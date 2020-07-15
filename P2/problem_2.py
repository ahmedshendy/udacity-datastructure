import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == None or path == None or len(suffix) < 1 or len(path) < 1:
        print("Invalied inputs")
        return []
    result_paths = []
    if os.path.exists(path):
        if os.path.isdir(path):
            for item in os.listdir(path):
                item = os.path.join(path, item)
                if os.path.isfile(item):
                    if item.endswith(suffix):
                        result_paths.append(item)
                else:
                    inner_result_paths = find_files(suffix, item)
                    if len(inner_result_paths) > 0:
                        result_paths.extend(inner_result_paths)
        else:
            if path.endswith(suffix):
                        result_paths.append(path)
    else:
        print("Path not exist")

    return result_paths

print(find_files('.c', 'testdir'))
# ['testdir\\subdir1\\a.c', 'testdir\\subdir3\\subsubdir1\\b.c', 'testdir\\subdir5\\a.c', 'testdir\\t1.c'] 

print(find_files('.c', 'notfoundDir'))
# Path not exist
# []

print(find_files('a.cc', 'testdir'))
# []

print(find_files('.c', 'testdir\\t1.c'))
# ['testdir\\t1.c']

print(find_files('a.cc', ''))
# Invalied inputs
# []

print(find_files('', 'testdir'))
# Invalied inputs
# []
