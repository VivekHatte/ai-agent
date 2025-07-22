import os

from configs import MAX_CHARS

def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)


    full_path = os.path.realpath(full_path)

    working_directory = os.path.realpath(working_directory)

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
  
    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    directory = os.path.realpath(directory)
    dir_contents = os.listdir(full_path)

    ret = ""
    for content in dir_contents:
        content_path = full_path + "/" + content
        ret += f'- {content}: file_size={os.path.getsize(content_path)}, is_dir={os.path.isdir(content_path)}\n'

    return ret[:-1]   

def get_file_content(working_directory, file_path):
   
    local_file_path = file_path

    file_path = os.path.join(working_directory, file_path)

    # print(full_path)

    file_path = os.path.realpath(file_path)
    print("File path: " + file_path)

    working_directory = os.path.realpath(working_directory)
    print(working_directory)

    if not file_path.startswith(working_directory):
        return f'Error: Cannot read "{local_file_path}" as it is outside the permitted working directory'



    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{local_file_path}"'
  
    try:

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            return file_content_string + ("" if len(file_content_string) < MAX_CHARS else f'[... File \"{local_file_path}\" truncated at {MAX_CHARS} characters]')
            
    except Exception as e:
        return f'Error: {e}'



    


