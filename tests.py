from functions.get_files_info import get_files_info


print(f'Results for current directory:')
print(get_files_info("calculator", "."))

print(f'Results for \'pkg\' directory:')
print(get_files_info("calculator", "pkg"))

print(f'Results for \'/bin\' directory:')
print(get_files_info("calculator", "/bin"))

print(f'Results for \'../\' directory:')
print(get_files_info("calculator", "../"))






