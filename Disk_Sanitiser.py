import sys
import os
import hashlib
import time
import datetime


def CalculateChecksum(FileName):

    with open(FileName, "rb") as fobj:

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while len(Buffer) > 0:
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):

    if not os.path.exists(DirectoryName):
        print("Path is Invalid")
        return None

    if not os.path.isdir(DirectoryName):
        print("It is not a Directory")
        return None

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        for fname in FileName:

            FilePath = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(FilePath)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(FilePath)
            else:
                Duplicate[Checksum] = [FilePath]

    return Duplicate


def DeleteDuplicate(DirectoryName):

    StartTime = time.time()

    MyDict = FindDuplicate(DirectoryName)

    if MyDict is None:
        return

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    TotalFiles = 0

    for value in MyDict.values():
        TotalFiles = TotalFiles + len(value)

    TotalDeleted = 0

    CurrentTime = datetime.datetime.now()

    LogFile = "DuplicateLog_" + CurrentTime.strftime(
        "%d_%m_%Y_%H_%M_%S"
    ) + ".txt"

    with open(LogFile, "w") as fobj:

        fobj.write("=========================================\n")
        fobj.write("        DUPLICATE FILE REPORT\n")
        fobj.write("=========================================\n\n")

        fobj.write(
            "Scan Date : " +
            CurrentTime.strftime("%d-%m-%Y") + "\n"
        )

        fobj.write(
            "Scan Time : " +
            CurrentTime.strftime("%H:%M:%S") + "\n"
        )

        fobj.write("Directory : " + DirectoryName + "\n")
        fobj.write("Total Files Scanned : " + str(TotalFiles) + "\n")
        fobj.write(
            "Duplicate Groups Found : " +
            str(len(Result)) + "\n\n"
        )

        fobj.write("Duplicate Files List\n")
        fobj.write("-----------------------------------------\n")

        for value in Result:

            fobj.write("\n")

            count = 0

            for subvalue in value:

                count = count + 1

                fobj.write(subvalue + "\n")

                if count > 1:
                    os.remove(subvalue)
                    TotalDeleted = TotalDeleted + 1

        EndTime = time.time()

        RequiredTime = EndTime - StartTime

        fobj.write("\n-----------------------------------------\n")
        fobj.write(
            "Total Duplicate Files Deleted : " +
            str(TotalDeleted) + "\n"
        )

        fobj.write(
            "Total Time Required : " +
            str(round(RequiredTime, 3)) +
            " Seconds\n"
        )

        fobj.write("-----------------------------------------\n")

    print("\n========== SUMMARY ==========")
    print("Total Files Scanned :", TotalFiles)
    print("Duplicate Groups :", len(Result))
    print("Total Deleted Files :", TotalDeleted)
    print("Time Required :", round(RequiredTime, 3), "Seconds")
    print("Log File Created Successfully :", LogFile)


def main():

    if len(sys.argv) != 2:
        print("Usage : python ProgramName.py DirectoryName")
        return

    DeleteDuplicate(sys.argv[1])


if __name__ == "__main__":
    main()
