import shutil

def __main__():
    resource_path = "/opt/vivaldi/resources/vivaldi"
    shutil.copy2(f"{resource_path}/style/common.css", f"{resource_path}/style/common_backup.css")

    with open(f"{resource_path}/style/common.css", 'w') as output:
        with open(f"{resource_path}/style/common_backup.css") as input:
            for line in input:
                output.write(line.replace("--color", "--custom"))

if __name__ == "__main__":
    __main__()

