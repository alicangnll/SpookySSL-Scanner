import platform, glob, sys, time, win32api

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_version_number(file_path):
    File_information = win32api.GetFileVersionInfo(file_path, "\\")
    ms_file_version = File_information['FileVersionMS']
    ls_file_version = File_information['FileVersionLS']
    return [str(win32api.HIWORD(ms_file_version)), str(win32api.LOWORD(ms_file_version)), str(win32api.HIWORD(ls_file_version)), str(win32api.LOWORD(ls_file_version))]

def scanlocal(disk):
    if(platform.system() == "Windows"):
        print("Finding DLL files...")
        dlllist = glob.glob('' + str(disk) + ':\\**\libssl*.dll', recursive=True)
        for file_path in dlllist:
            version = ".".join(get_version_number(file_path))
            if("1.1.1.0" <= version <= "1.1.1.99"):
                print(bcolors.OKGREEN + file_path + " (" + version + ") IS NOT VULNERABLE!" + bcolors.ENDC)
            elif("3.0.0.0" <= version <= "3.0.6.9"):
                print(bcolors.WARNING + file_path + " (" + version + ") IS VULNERABLE!" + bcolors.ENDC)
            elif(version > "3.0.6.9"):
                print(bcolors.OKGREEN + file_path + " (" + version + ") IS NOT VULNERABLE!" + bcolors.ENDC)
            elif(version < "1.1.1.0"):
                print(bcolors.OKCYAN + file_path + " (" + version + ") IS NOT FOUND!" + bcolors.ENDC)
            else:
                print("NOT FOUND (" + file_path + " | " + version + ")")
    else:
        import osquery
        instance = osquery.SpawnInstance()
        instance.open()
        print("Scanning for Debian-based...")
        print(instance.client.query('select name, version from deb_packages where name like "openssl" and version like "3.0%"; > spookyssl-logs.log'))
        print("Scanning for RHEL-based...")
        print(instance.client.query('select name, version from rpm_packages where name like "openssl" and version like "3.0%"; > spookyssl-logs.log'))
        print("Scanning for macOS...")
        print(instance.client.query('SELECT * FROM homebrew_packages WHERE name LIKE "openssl" and version like "3.0%"; > spookyssl-logs.log'))

print("====================================================")
print(" SpookySSL CVE-2022-3602 SSLv3 Scanner (11-02-2022) ")
print("====================================================")
disk = input("Write your disk name (ex. C, D) : ")
scanlocal(disk)
time.sleep(5000)
sys.exit(0)
