def main():
    types={"gif":"image/gif","jpg":"image/jpeg","jpeg":"image/jpeg","png":"image/png",
           "pdf":"application/pdf","txt":"text/plain","zip":"application/zip"}
    try:
        file=str(input("File name: "))
        list=file.split(".")
        ext=list[1]
        if ext in types:
            print(types[ext])
        else: print("application/octet-stream")
    except IndexError:
        print("application/octet-stream")
main()