import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A8DXWi9M5vGeSA2s0rAu-3V9hQKt_mrxwdwWQwLgLSe5Zx8eFMbUpPV9SeueRiJtLdzUayLDBGQLLA9nPyT5UExGm4FPKg0hinfkExSl4scvdycJOXcm6f7Tn2vjRQIFw_aGPeM'
    transferData = TransferData(access_token)

    file_from = input("enter the path to transfer")
    file_to = input("enter the full path ")

     # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
