#!/usr/bin/env python3
"""
M1.5: Generate Dashboard - MEARA Pipeline Step 5

This script injects structured JavaScript data into HTML templates to create
the final interactive marketing analysis dashboard.

Usage:
    python M1.5_generate_dashboard.py --data_file extracted_data.js --output_dir dashboard/
    
Requirements:
    - HTML templates in docs_framework/07_html_templates/
    - Extracted JavaScript data file from M1.4
    - Output directory for generated dashboard files
"""

import os
import re
import json
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Any


class DashboardGenerator:
    """Generates interactive HTML dashboard from MEARA analysis data."""
    
    def __init__(self, template_dir: str, output_dir: str):
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.data = {}
        
    def load_data(self, data_file: str) -> None:
        """Load JavaScript data file and parse into Python objects."""
        print(f"Loading data from {data_file}...")
        
        with open(data_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Parse JavaScript objects into Python data
        self.data = self._parse_js_data(js_content)
        print(f"✓ Loaded data for {self.data.get('companyInfo', {}).get('name', 'Unknown Company')}")
        
    def _parse_js_data(self, js_content: str) -> Dict[str, Any]:
        """Parse JavaScript data into Python dictionaries."""
        data = {}
        
        # Extract company info
        company_match = re.search(r'const companyInfo = ({.*?});', js_content, re.DOTALL)
        if company_match:
            # Convert JS object to JSON-like format and parse
            js_obj = company_match.group(1)
            # Simple conversion - in production, use proper JS parser
            js_obj = re.sub(r'(\w+):', r'"\1":', js_obj)  # Add quotes to keys
            try:
                data['companyInfo'] = json.loads(js_obj)
            except json.JSONDecodeError:
                # Fallback: extract manually
                data['companyInfo'] = self._extract_company_info(js_content)
        
        # Extract dimension ratings
        ratings_match = re.search(r'const dimensionRatings = (\[.*?\]);', js_content, re.DOTALL)
        if ratings_match:
            data['dimensionRatings'] = self._extract_dimension_ratings(js_content)
        
        # Extract dimension analysis data
        for i in range(1, 10):
            pattern = f'const dimension{i}AnalysisData = (\\[.*?\\]);'
            match = re.search(pattern, js_content, re.DOTALL)
            if match:
                data[f'dimension{i}AnalysisData'] = self._extract_analysis_data(match.group(1))
        
        # Extract strategic recommendations
        recommendations_match = re.search(r'const strategicRecommendations = (\[.*?\]);', js_content, re.DOTALL)
        if recommendations_match:
            data['strategicRecommendations'] = self._extract_recommendations(js_content)
        
        return data
    
    def _extract_company_info(self, js_content: str) -> Dict[str, str]:
        """Extract company info manually."""
        info = {}
        
        name_match = re.search(r'name:\s*"([^"]*)"', js_content)
        if name_match:
            info['name'] = name_match.group(1)
            
        industry_match = re.search(r'industry:\s*"([^"]*)"', js_content)
        if industry_match:
            info['industry'] = industry_match.group(1)
            
        challenge_match = re.search(r'primaryChallenge:\s*"([^"]*)"', js_content)
        if challenge_match:
            info['primaryChallenge'] = challenge_match.group(1)
            
        date_match = re.search(r'analysisDate:\s*"([^"]*)"', js_content)
        if date_match:
            info['analysisDate'] = date_match.group(1)
        
        return info
    
    def _extract_dimension_ratings(self, js_content: str) -> List[Dict[str, str]]:
        """Extract dimension ratings array."""
        ratings = []
        
        # Find all dimension rating objects
        pattern = r'{\s*name:\s*"([^"]*)",\s*rating:\s*"([^"]*)",\s*file:\s*"([^"]*)"\s*}'
        matches = re.findall(pattern, js_content)
        
        for name, rating, file in matches:
            ratings.append({
                'name': name,
                'rating': rating,
                'file': file
            })
        
        return ratings
    
    def _extract_analysis_data(self, js_array: str) -> List[Dict[str, Any]]:
        """Extract analysis data for a dimension."""
        # Simplified extraction - in production, use proper JS parser
        data = []
        
        # This is a simplified version - would need robust JS parsing for production
        # For now, return empty array as placeholder
        return data
    
    def _extract_recommendations(self, js_content: str) -> List[Dict[str, Any]]:
        """Extract strategic recommendations."""
        # Simplified extraction - return empty array as placeholder
        return []
    
    def generate_dashboard(self) -> None:
        """Generate complete dashboard from templates and data."""
        print("Generating dashboard...")
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy static assets
        self._copy_static_assets()
        
        # Generate main index page
        self._generate_index_page()
        
        # Generate dimension pages
        self._generate_dimension_pages()
        
        print(f"✓ Dashboard generated in {self.output_dir}")
        print(f"  Open {self.output_dir}/index.html to view")
    
    def _copy_static_assets(self) -> None:
        """Copy CSS and other static assets."""
        css_file = self.template_dir / "branding.css"
        if css_file.exists():
            shutil.copy2(css_file, self.output_dir / "branding.css")
            print("✓ Copied branding.css")
    
    def _generate_index_page(self) -> None:
        """Generate main dashboard index page."""
        template_file = self.template_dir / "index.template.html"
        
        if not template_file.exists():
            print(f"✗ Template not found: {template_file}")
            return
        
        # Read template
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Replace placeholders
        company_info = self.data.get('companyInfo', {})
        
        html = template.replace('{{company_name}}', company_info.get('name', 'Company'))
        html = html.replace('{{deep_research_report_url}}', '#')  # Placeholder
        html = html.replace('{{full_analysis_report_url}}', '#')  # Placeholder
        
        # Inject dimension ratings data
        dimension_ratings = self.data.get('dimensionRatings', [])
        ratings_js = self._format_js_array(dimension_ratings)
        html = html.replace('/* {{dimension_ratings_js_array}} */ []', ratings_js)
        
        # Write output
        output_file = self.output_dir / "index.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print("✓ Generated index.html")
    
    def _generate_dimension_pages(self) -> None:
        """Generate individual dimension analysis pages."""
        template_file = self.template_dir / "dimension.template.html"
        
        if not template_file.exists():
            print(f"✗ Template not found: {template_file}")
            return
        
        # Read template
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
        
        dimension_ratings = self.data.get('dimensionRatings', [])
        company_info = self.data.get('companyInfo', {})
        
        for i, dimension in enumerate(dimension_ratings, 1):
            # Replace placeholders
            html = template.replace('{{company_name}}', company_info.get('name', 'Company'))
            html = html.replace('{{dimension_name}}', dimension['name'])
            html = html.replace('{{overall_rating}}', dimension['rating'])
            
            # Set rating CSS classes
            rating_css = self._get_rating_css(dimension['rating'])
            html = html.replace('{{overall_rating_css}}', rating_css['bg'])
            html = html.replace('{{overall_rating_text_css}}', rating_css['text'])
            
            # Inject analysis data
            analysis_data = self.data.get(f'dimension{i}AnalysisData', [])
            analysis_js = self._format_js_array(analysis_data)
            html = html.replace('/* {{analysis_data_js_array}} */ []', analysis_js)
            
            # Add navigation options (simplified)
            nav_options = self._generate_nav_options(dimension_ratings, i)
            html = html.replace('<!--{{dimension_nav_options}}-->', nav_options)
            
            # Placeholder URLs
            html = html.replace('{{deep_research_report_url}}', '#')
            html = html.replace('{{full_analysis_report_url}}', '#')
            
            # Write output
            output_file = self.output_dir / f"dimension_{i}.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
        
        print(f"✓ Generated {len(dimension_ratings)} dimension pages")
    
    def _get_rating_css(self, rating: str) -> Dict[str, str]:
        """Get CSS classes for rating."""
        rating_map = {
            'Exceptional': {'bg': 'bg-exceptional border-exceptional', 'text': 'text-exceptional'},
            'Competent': {'bg': 'bg-competent border-competent', 'text': 'text-competent'},
            'Needs Work': {'bg': 'bg-needs-improvement border-needs-improvement', 'text': 'text-needs-improvement'},
            'Critical Gap': {'bg': 'bg-critical border-critical', 'text': 'text-critical'}
        }
        return rating_map.get(rating, {'bg': 'bg-gray-100', 'text': 'text-gray-700'})
    
    def _generate_nav_options(self, dimensions: List[Dict], current_index: int) -> str:
        """Generate navigation options for dimension selector."""
        options = []
        for i, dim in enumerate(dimensions, 1):
            selected = "selected" if i == current_index else ""
            options.append(f'<option value="dimension_{i}.html" {selected}>{dim["name"]}</option>')
        return '\n'.join(options)
    
    def _format_js_array(self, data: List[Dict[str, Any]]) -> str:
        """Format Python data as JavaScript array."""
        if not data:
            return '[]'
        
        # Convert to JSON and format for JavaScript
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        return json_str


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Generate MEARA dashboard from analysis data')
    parser.add_argument('--data_file', required=True, help='JavaScript data file from M1.4')
    parser.add_argument('--template_dir', default='../docs_framework/07_html_templates', 
                       help='Directory containing HTML templates')
    parser.add_argument('--output_dir', default='./dashboard', 
                       help='Output directory for generated dashboard')
    
    args = parser.parse_args()
    
    # Validate inputs
    if not os.path.exists(args.data_file):
        print(f"✗ Data file not found: {args.data_file}")
        return 1
    
    if not os.path.exists(args.template_dir):
        print(f"✗ Template directory not found: {args.template_dir}")
        return 1
    
    # Generate dashboard
    generator = DashboardGenerator(args.template_dir, args.output_dir)
    
    try:
        generator.load_data(args.data_file)
        generator.generate_dashboard()
        print("\n✅ Dashboard generation complete!")
        print(f"📊 Open {args.output_dir}/index.html in your browser")
        
    except Exception as e:
        print(f"✗ Error generating dashboard: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())