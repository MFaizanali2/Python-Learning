import os

def list_files_only(path='/'):
    try:
        for name in os.listdir(path):
            full = os.path.join(path, name)
            if os.path.isfile(full):
                print(name)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_files_only('.')
