class Utils(object):
    def get_common_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def common_headers_xml(self):
        return {
            "Content-Type": "application/xml",
        }

    def common_header_put_delete_patch_cookie(self, token):
        return {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
