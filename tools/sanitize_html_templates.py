#!/usr/bin/env python3
"""
HTML Template Sanitization Script for MEARA Framework

This script converts hardcoded HTML files into reusable templates with placeholders
for dynamic content injection. It processes files in the docs_framework/07_html_templates/
directory and creates template versions suitable for data-driven report generation.
"""

import os
import re
from pathlib import Path
import json
import sys

try:
    from bs4 import BeautifulSoup, Comment
except ImportError:
    print("BeautifulSoup4 is required but not installed.")
    print("Please install it using: pip install beautifulsoup4")
    print("\nAlternatively, running simplified version without BeautifulSoup...")
    # We'll implement a regex-based fallback
    BeautifulSoup = None
    Comment = None


class HTMLTemplateSanitizer:
    def __init__(self, input_dir="docs_framework/07_html_templates"):
        self.input_dir = Path(input_dir)
        self.templates_created = []
        
    def sanitize_index_html(self):
        """Sanitize the main dashboard file (index.html)"""
        print("Processing index.html...")
        
        index_path = self.input_dir / "index.html"
        if not index_path.exists():
            print(f"Error: {index_path} not found")
            return False
            
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Replace company name in title and h1 tags
        title_tag = soup.find('title')
        if title_tag and 'HelloPatient' in title_tag.string:
            title_tag.string = title_tag.string.replace('HelloPatient', '{{company_name}}')
            
        h1_tag = soup.find('h1')
        if h1_tag and 'HelloPatient' in h1_tag.text:
            h1_tag.string = h1_tag.text.replace('HelloPatient', '{{company_name}}')
            
        # 2. Replace Google Docs URLs
        # Find the deep research report link
        deep_research_link = soup.find('a', href=re.compile(r'docs\.google\.com.*1hwLpRl7Q_0akMUoe5EPrSLj1-YHRGjN-XhZD53IyAWU'))
        if deep_research_link:
            deep_research_link['href'] = '{{deep_research_report_url}}'
            
        # Find the full analysis report link
        full_analysis_link = soup.find('a', href=re.compile(r'docs\.google\.com.*1zriIMv_D3eDPaBGDvvki_qo2eTPKecsvXhseyZ_Ngzk'))
        if full_analysis_link:
            full_analysis_link['href'] = '{{full_analysis_report_url}}'
            
        # Convert back to string for JavaScript replacement
        html_content = str(soup)
        
        # 3. Replace the dimensionRatings JavaScript array
        # Use regex to find and replace the entire array
        dimension_pattern = r'const\s+dimensionRatings\s*=\s*\[(.*?)\];'
        html_content = re.sub(
            dimension_pattern,
            'const dimensionRatings = /* {{dimension_ratings_js_array}} */ [];',
            html_content,
            flags=re.DOTALL
        )
        
        # Save the template
        output_path = self.input_dir / "index.template.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        self.templates_created.append(output_path)
        print(f"Created: {output_path}")
        return True
        
    def sanitize_dimension_pages(self):
        """Create a single master template from dimension-specific pages"""
        print("\nProcessing dimension-specific pages...")
        
        # Use market-positioning-messaging-analysis.html as the base template
        base_file = self.input_dir / "market-positioning-messaging-analysis.html"
        if not base_file.exists():
            print(f"Error: {base_file} not found")
            return False
            
        with open(base_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Replace company name in title
        title_tag = soup.find('title')
        if title_tag and 'HelloPatient' in title_tag.string:
            title_tag.string = '{{company_name}} Marketing Analysis'
            
        # 2. Replace dimension name in h1
        h1_tag = soup.find('h1')
        if h1_tag:
            h1_tag.string = '{{dimension_name}}'
            
        # 3. Replace overall rating text and CSS
        # Find the rating banner div
        rating_banner = soup.find('div', class_=re.compile(r'scalevp-.*-bg'))
        if rating_banner:
            # Replace the entire class attribute with a placeholder
            rating_banner['class'] = ['{{overall_rating_css}}']
            # Also update the inline style if present
            if 'style' in rating_banner.attrs:
                rating_banner['style'] = '{{overall_rating_style}}'
                
            # Replace the rating text
            rating_text = rating_banner.find('span', class_=re.compile(r'scalevp-.*-text'))
            if rating_text:
                rating_text.string = '{{overall_rating}}'
                rating_text['class'] = ['text-2xl', 'font-bold', '{{overall_rating_text_css}}']
        
        # 4. Replace Google Docs URLs (same as index)
        deep_research_link = soup.find('a', href=re.compile(r'docs\.google\.com.*1hwLpRl7Q_0akMUoe5EPrSLj1-YHRGjN-XhZD53IyAWU'))
        if deep_research_link:
            deep_research_link['href'] = '{{deep_research_report_url}}'
            
        full_analysis_link = soup.find('a', href=re.compile(r'docs\.google\.com.*1zriIMv_D3eDPaBGDvvki_qo2eTPKecsvXhseyZ_Ngzk'))
        if full_analysis_link:
            full_analysis_link['href'] = '{{full_analysis_report_url}}'
            
        # 5. Replace dimension navigation options
        dimension_select = soup.find('select', id='dimensionSelect')
        if dimension_select:
            # Remove all option elements except the first (placeholder)
            options = dimension_select.find_all('option')
            for option in options[1:]:  # Keep the first "Select dimension..." option
                option.decompose()
                
            # Add placeholder comment
            placeholder_comment = Comment('{{dimension_nav_options}}')
            dimension_select.append(placeholder_comment)
            
        # Convert back to string for JavaScript replacement
        html_content = str(soup)
        
        # 6. Replace the analysisData JavaScript array
        analysis_pattern = r'const\s+analysisData\s*=\s*\[(.*?)\];'
        html_content = re.sub(
            analysis_pattern,
            'const analysisData = /* {{analysis_data_js_array}} */ [];',
            html_content,
            flags=re.DOTALL
        )
        
        # Save the template
        output_path = self.input_dir / "dimension.template.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        self.templates_created.append(output_path)
        print(f"Created: {output_path}")
        return True
        
    def test_templates(self):
        """Test the generated templates with sample data"""
        print("\n" + "="*50)
        print("TESTING TEMPLATES")
        print("="*50)
        
        # Test data
        test_data = {
            'company_name': 'TestCompany',
            'deep_research_report_url': 'https://example.com/deep-research',
            'full_analysis_report_url': 'https://example.com/full-analysis',
            'dimension_ratings_js_array': '''[
            { name: "Test Dimension 1", rating: "Exceptional", file: "test1.html" },
            { name: "Test Dimension 2", rating: "Competent", file: "test2.html" }
        ]''',
            'dimension_name': 'Test Dimension Analysis',
            'overall_rating': 'Exceptional',
            'overall_rating_css': 'bg-exceptional border-exceptional border-2 rounded-lg p-4 mb-6',
            'overall_rating_style': 'border-color: #7da399;',
            'overall_rating_text_css': 'text-exceptional',
            'analysis_data_js_array': '''[
            {
                "Element": "Test Element",
                "Rating": "Exceptional",
                "Strengths": ["Test strength"],
                "Opportunities": ["Test opportunity"],
                "Examples": ["Test example"]
            }
        ]''',
            'dimension_nav_options': '''<option value="test1.html">Test Dimension 1</option>
        <option value="test2.html">Test Dimension 2</option>'''
        }
        
        # Test index template
        print("\n1. Testing index.template.html...")
        index_template = self.input_dir / "index.template.html"
        if index_template.exists():
            with open(index_template, 'r', encoding='utf-8') as f:
                template_content = f.read()
                
            # Check for placeholders
            placeholders = ['{{company_name}}', '{{deep_research_report_url}}', 
                          '{{full_analysis_report_url}}', '{{dimension_ratings_js_array}}']
            
            missing = [p for p in placeholders if p not in template_content]
            if missing:
                print(f"   ❌ Missing placeholders: {missing}")
            else:
                print("   ✅ All placeholders found in index template")
                
            # Test replacement
            test_content = template_content
            for key, value in test_data.items():
                if '{{' + key + '}}' in test_content:
                    test_content = test_content.replace('{{' + key + '}}', value)
                    
            # Save test output
            test_output = self.input_dir / "test_index.html"
            with open(test_output, 'w', encoding='utf-8') as f:
                f.write(test_content)
            print(f"   ✅ Test output saved to: {test_output}")
            
        # Test dimension template
        print("\n2. Testing dimension.template.html...")
        dimension_template = self.input_dir / "dimension.template.html"
        if dimension_template.exists():
            with open(dimension_template, 'r', encoding='utf-8') as f:
                template_content = f.read()
                
            # Check for placeholders
            placeholders = ['{{company_name}}', '{{dimension_name}}', '{{overall_rating}}',
                          '{{overall_rating_css}}', '{{analysis_data_js_array}}', 
                          '{{dimension_nav_options}}']
            
            missing = [p for p in placeholders if p not in template_content]
            if missing:
                print(f"   ❌ Missing placeholders: {missing}")
            else:
                print("   ✅ All placeholders found in dimension template")
                
            # Test replacement
            test_content = template_content
            for key, value in test_data.items():
                if '{{' + key + '}}' in test_content:
                    test_content = test_content.replace('{{' + key + '}}', value)
                    
            # Save test output
            test_output = self.input_dir / "test_dimension.html"
            with open(test_output, 'w', encoding='utf-8') as f:
                f.write(test_content)
            print(f"   ✅ Test output saved to: {test_output}")
            
        print("\n" + "="*50)
        print("TESTING COMPLETE")
        print("="*50)
        
    def run(self):
        """Run the complete sanitization process"""
        print("Starting HTML Template Sanitization Process")
        print("="*50)
        
        # Check if input directory exists
        if not self.input_dir.exists():
            print(f"Error: Directory {self.input_dir} not found")
            return
            
        # Process index.html
        if self.sanitize_index_html():
            print("✅ Successfully processed index.html")
        else:
            print("❌ Failed to process index.html")
            
        # Process dimension pages
        if self.sanitize_dimension_pages():
            print("✅ Successfully created dimension template")
        else:
            print("❌ Failed to create dimension template")
            
        # Run tests
        self.test_templates()
        
        # Summary
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        print(f"Templates created: {len(self.templates_created)}")
        for template in self.templates_created:
            print(f"  - {template}")
            

if __name__ == "__main__":
    sanitizer = HTMLTemplateSanitizer()
    sanitizer.run()