import os



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
