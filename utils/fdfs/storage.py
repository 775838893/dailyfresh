from django.core.files.storage import Storage
from django.conf import settings
from fdfs_client.client import Fdfs_client


class FDFSStorage(Storage):

    def __init__(self, client_conf=None, base_url=None):

        if not client_conf:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if not base_url:
            base_url = settings.FDFS_URL
        self.base_url = base_url


    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        client = Fdfs_client(self.client_conf)

        res = client.upload_by_buffer(content.read())

        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast dfs失败')

        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        '''Django判断文件名是否可用'''
        return False

    def url(self, name):
        '''返回访问文件的url路径'''
        return self.base_url + name
