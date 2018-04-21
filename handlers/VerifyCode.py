# coding:utf-8

import logging
import constants

from utils.captcha.captcha import captcha
from .BaseHandler import BaseHandler

class ImageCodeHandler(BaseHandler):
    """ """
    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redis.delete("")
            except Exception as e:
                logging.error(e)
        # name 图片验证码名称
        # text 图片验证码文本
        # image 图片验证码二进制数据
        name,text,image = captcha.generate_captcha()
        try:
            self.redis.settex("image_code %s"%code_id,constants.IMAGE_CODE_EXPIRES_SECONDS,text)
        except Exception as e:
            logging.error(e)
            self.write("")
        self.set_header("Content-Type","image/jpg")
        self.write(image)


