import os
import pandas as pd

def load_funcom_dataset(data_folder):
    java_files = []
    comments = []

    # Traverse the directory to find all Java files and their comments
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    java_files.append(f.read())
                
                # Here, we assume that each Java file has an associated comment file
                comment_file_path = file_path.replace('.java', '.comment')
                if os.path.exists(comment_file_path):
                    with open(comment_file_path, 'r') as cf:
                        comments.append(cf.read())
                else:
                    comments.append('')

    # Create a DataFrame
    dataset = pd.DataFrame({'code': java_files, 'comment': comments})

    return dataset

# Usage
data_folder = 'path_to_extracted_funcom'
dataset = load_funcom_dataset(data_folder)
print(dataset.head())
