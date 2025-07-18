#!/usr/bin/env python3
"""
HTML Template Sanitization Script for MEARA Framework (Simplified Version)

This script converts hardcoded HTML files into reusable templates with placeholders
for dynamic content injection. It uses regex patterns for all replacements.
"""

import os
import re
from pathlib import Path


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
            
        # 1. Replace company name in title tag
        content = re.sub(
            r'<title>HelloPatient([^<]*)</title>',
            r'<title>{{company_name}}\1</title>',
            content
        )
        
        # 2. Replace company name in h1 tag
        content = re.sub(
            r'(<h1[^>]*>)\s*HelloPatient:\s*([^<]*</h1>)',
            r'\1{{company_name}}: \2',
            content
        )
        
        # 3. Replace Google Docs URLs
        # Deep research report
        content = re.sub(
            r'href="https://docs\.google\.com/document/d/1hwLpRl7Q_0akMUoe5EPrSLj1-YHRGjN-XhZD53IyAWU/edit"',
            'href="{{deep_research_report_url}}"',
            content
        )
        
        # Full analysis report
        content = re.sub(
            r'href="https://docs\.google\.com/document/d/1zriIMv_D3eDPaBGDvvki_qo2eTPKecsvXhseyZ_Ngzk/edit"',
            'href="{{full_analysis_report_url}}"',
            content
        )
        
        # 4. Replace the dimensionRatings JavaScript array
        dimension_pattern = r'const\s+dimensionRatings\s*=\s*\[(.*?)\];'
        content = re.sub(
            dimension_pattern,
            'const dimensionRatings = {{dimension_ratings_js_array}};',
            content,
            flags=re.DOTALL
        )
        
        # Save the template
        output_path = self.input_dir / "index.template.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
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
            
        # 1. Replace company name in title
        content = re.sub(
            r'<title>HelloPatient[^<]*</title>',
            '<title>{{company_name}} Marketing Analysis</title>',
            content
        )
        
        # 2. Replace dimension name in h1
        content = re.sub(
            r'<h1[^>]*>\s*Marketing Positioning & Messaging Analysis\s*</h1>',
            '<h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4 text-center">{{dimension_name}}</h1>',
            content
        )
        
        # 3. Replace overall rating banner
        # Find and replace the rating div with its classes
        content = re.sub(
            r'<div class="scalevp-needs-improvement-bg scalevp-needs-improvement-border[^"]*"[^>]*>',
            '<div class="{{overall_rating_css}}">',
            content
        )
        
        # Replace the rating text
        content = re.sub(
            r'<span class="[^"]*scalevp-needs-improvement-text[^"]*">Needs Improvement</span>',
            '<span class="text-2xl font-bold {{overall_rating_text_css}}">{{overall_rating}}</span>',
            content
        )
        
        # 4. Replace Google Docs URLs (same as index)
        content = re.sub(
            r'href="https://docs\.google\.com/document/d/1hwLpRl7Q_0akMUoe5EPrSLj1-YHRGjN-XhZD53IyAWU/edit"',
            'href="{{deep_research_report_url}}"',
            content
        )
        
        content = re.sub(
            r'href="https://docs\.google\.com/document/d/1zriIMv_D3eDPaBGDvvki_qo2eTPKecsvXhseyZ_Ngzk/edit"',
            'href="{{full_analysis_report_url}}"',
            content
        )
        
        # 5. Replace dimension navigation options
        # Find the select element and replace all options except the first
        select_pattern = r'(<select[^>]*id="dimensionSelect"[^>]*>.*?<option[^>]*>Select dimension\.\.\.</option>)(.*?)(</select>)'
        content = re.sub(
            select_pattern,
            r'\1\n                        {{dimension_nav_options}}\n                    \3',
            content,
            flags=re.DOTALL
        )
        
        # 6. Replace the analysisData JavaScript array
        analysis_pattern = r'const\s+analysisData\s*=\s*\[(.*?)\];'
        content = re.sub(
            analysis_pattern,
            'const analysisData = {{analysis_data_js_array}};',
            content,
            flags=re.DOTALL
        )
        
        # 7. Update the specific company reference in the paragraph
        content = re.sub(
            r"HelloPatient's Market Positioning & Messaging",
            "{{company_name}}'s {{dimension_name}}",
            content
        )
        
        # Save the template
        output_path = self.input_dir / "dimension.template.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
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
                
            # Count placeholder occurrences
            for p in placeholders:
                count = template_content.count(p)
                print(f"   - {p}: {count} occurrence(s)")
                
        # Test dimension template
        print("\n2. Testing dimension.template.html...")
        dimension_template = self.input_dir / "dimension.template.html"
        if dimension_template.exists():
            with open(dimension_template, 'r', encoding='utf-8') as f:
                template_content = f.read()
                
            # Check for placeholders
            placeholders = ['{{company_name}}', '{{dimension_name}}', '{{overall_rating}}',
                          '{{overall_rating_css}}', '{{overall_rating_text_css}}',
                          '{{analysis_data_js_array}}', '{{dimension_nav_options}}']
            
            missing = [p for p in placeholders if p not in template_content]
            if missing:
                print(f"   ❌ Missing placeholders: {missing}")
            else:
                print("   ✅ All placeholders found in dimension template")
                
            # Count placeholder occurrences
            for p in placeholders:
                count = template_content.count(p)
                print(f"   - {p}: {count} occurrence(s)")
                
        # Create test outputs
        print("\n3. Creating test outputs...")
        
        # Test index
        if index_template.exists():
            with open(index_template, 'r', encoding='utf-8') as f:
                test_content = f.read()
                
            for key, value in test_data.items():
                placeholder = '{{' + key + '}}'
                if placeholder in test_content:
                    test_content = test_content.replace(placeholder, value)
                    
            test_output = self.input_dir / "test_index.html"
            with open(test_output, 'w', encoding='utf-8') as f:
                f.write(test_content)
            print(f"   ✅ Test output saved to: {test_output}")
            
        # Test dimension
        if dimension_template.exists():
            with open(dimension_template, 'r', encoding='utf-8') as f:
                test_content = f.read()
                
            for key, value in test_data.items():
                placeholder = '{{' + key + '}}'
                if placeholder in test_content:
                    test_content = test_content.replace(placeholder, value)
                    
            test_output = self.input_dir / "test_dimension.html"
            with open(test_output, 'w', encoding='utf-8') as f:
                f.write(test_content)
            print(f"   ✅ Test output saved to: {test_output}")
            
        print("\n" + "="*50)
        print("TESTING COMPLETE")
        print("="*50)
        
    def run(self):
        """Run the complete sanitization process"""
        print("Starting HTML Template Sanitization Process (Simplified Version)")
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