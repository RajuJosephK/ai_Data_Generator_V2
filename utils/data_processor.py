import json
import io
import csv

def convert_to_csv(content):
    """
    Convert JSON content to CSV format
    Returns: (csv_content, success_flag)
    """
    try:
        data = json.loads(content)
        
        if isinstance(data, list) and len(data) > 0:
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            csv_content = output.getvalue()
            return csv_content, True
        else:
            return None, False
            
    except Exception as e:
        return None, False

def format_json(content):
    """Pretty print JSON content"""
    try:
        data = json.loads(content)
        return json.dumps(data, indent=2)
    except:
        return content

def validate_json(content):
    """Check if content is valid JSON"""
    try:
        json.loads(content)
        return True
    except:
        return False