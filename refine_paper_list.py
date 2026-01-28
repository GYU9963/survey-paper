import pandas as pd
import re

# File paths
input_csv = 'Paper_Placement_Plan.csv'
output_csv = 'Paper_Placement_Plan.csv'

def clean_and_update_structure():
    try:
        # Load the CSV
        df = pd.read_csv(input_csv)
        print(f"Loaded {len(df)} papers.")

        # 1. Filter Excluded papers
        if 'Excluded' in df.columns:
            initial_count = len(df)
            df = df[df['Excluded'] != 'Y']
            print(f"Removed {initial_count - len(df)} excluded papers (marked 'Y').")
            # Drop the Excluded column as it's no longer needed
            df = df.drop(columns=['Excluded'])
        
        # 2. Remove Duplicates
        # Normalize title for comparison
        df['Title_Lower'] = df['Title'].astype(str).str.lower().str.strip()
        initial_count = len(df)
        df = df.drop_duplicates(subset='Title_Lower', keep='first')
        print(f"Removed {initial_count - len(df)} duplicate papers.")
        df = df.drop(columns=['Title_Lower'])

        # 3. Define New Structure Mapping
        # Map sub-section prefixes (e.g., "2.1") to new Section Names
        # Map main section prefixes (e.g., "2") to new Parent Section Names
        
        section_map = {
            '1.1': '1.1 Overview & Scope',
            '2.1': '2.1 Robotic Platforms & Kinematics',
            '2.2': '2.2 Material Behavior & Process Parameters',
            '3.1': '3.1 Sensing Modalities',
            '4.1': '4.1 Quality Monitoring & Diagnosis',
            '4.2': '4.2 Intelligent Path Planning',
            '5.1': '5.1 Feedback Control Systems',
            '5.2': '5.2 Surface Finishing & Integration'
        }

        parent_map = {
            '1': '1. Introduction',
            '2': '2. The Physical Layer: Robotic Platforms & Material Dynamics',
            '3': '3. The Perception Layer: In-Process Sensing & Digitalization',
            '4': '4. The Cognitive Layer: AI-Driven Diagnosis & Path Planning',
            '5': '5. The Execution Layer: Closed-Loop Control & Automated Finishing',
            '6': '6. Conclusion: Towards Cognitive Autonomous Construction'
        }

        # Function to update section info
        def update_hierarchy(row):
            # Extract subsection number from Subsection column (e.g., "2.1.1 ...")
            # Fallback to Section column if Subsection is missing or "-"
            
            sub_str = str(row['Subsection'])
            sec_str = str(row['Section'])
            
            # Try to find a pattern like X.Y.Z
            match = re.match(r'(\d+\.\d+)\.\d+', sub_str)
            if not match:
                # Try X.Y from Section column
                match_sec = re.match(r'(\d+\.\d+)', sec_str)
                if match_sec:
                    prefix = match_sec.group(1)
                else:
                    # Try to parse from Subsection if it's just X.Y (unlikely but possible)
                    match_sub_short = re.match(r'(\d+\.\d+)', sub_str)
                    if match_sub_short:
                        prefix = match_sub_short.group(1)
                    else:
                        # Fallback based on Parent Section
                        prefix = str(row['Parent_Section']) + ".1" # Default to .1 if unknown?
            else:
                prefix = match.group(1)
            
            # Get main section number (X)
            main_num = prefix.split('.')[0]
            
            # Update fields
            new_section_name = section_map.get(prefix, row['Section'])
            new_parent_name = parent_map.get(main_num, row['Parent_Section'])
            
            return pd.Series([new_parent_name, new_section_name])

        # Apply mapping
        df[['Parent_Section', 'Section']] = df.apply(update_hierarchy, axis=1)

        # 4. Sorting
        # Sort by Subsection (alphanumeric sort might be tricky, but standard sort usually works for 2.1.1 vs 2.1.2)
        # We want natural sort for sections
        
        # Helper for sorting
        def sort_key(s):
            # Extract first number group
            s = str(s)
            parts = re.findall(r'\d+', s)
            return [int(p) for p in parts] if parts else [999]

        df['Sort_Key'] = df['Subsection'].apply(sort_key)
        df = df.sort_values('Sort_Key')
        df = df.drop(columns=['Sort_Key'])

        # 5. Save
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')
        print(f"Successfully saved {len(df)} papers to {output_csv}")
        
        # Verify counts
        print("\nPaper Counts by Parent Section:")
        print(df['Parent_Section'].value_counts())

    except PermissionError:
        print("Error: Permission denied. Please close the CSV file in Excel and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clean_and_update_structure()
