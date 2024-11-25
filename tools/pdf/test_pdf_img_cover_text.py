# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
import os
import sys
import fitz  # PyMuPDF
from fpdf import FPDF
from dotenv import load_dotenv
import json

# 加载 .env 文件
load_dotenv()

# 获取环境变量
access_key_id = os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID')
access_key_secret = os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET')


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> ocr_api20210707Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        config.endpoint = 'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def recognize_image(client, image_path):
        body_stream = StreamClient.read_from_file_path(image_path)
        recognize_general_request = ocr_api_20210707_models.RecognizeGeneralRequest(
            body=body_stream
        )
        runtime = util_models.RuntimeOptions()
        try:
            response = client.recognize_general_with_options(recognize_general_request, runtime)
            # print(f"Response data: {response.body.data.content}")  # 打印响应数据
            if isinstance(response.body.data, str):
                response_data = json.loads(response.body.data)
            else:
                response_data = response.body.data
            return response_data
        except Exception as error:
            print(f"Error: {str(error)}")
            if hasattr(error, 'data') and error.data.get("Recommend"):
                print(f"Recommend: {error.data.get('Recommend')}")
            return []

    @staticmethod
    def process_pdf(input_pdf_path, output_pdf_path):
        client = Sample.create_client()
        doc = fitz.open(input_pdf_path)
        pdf = FPDF('P', 'mm', 'A4')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_font('AlibabaPuHuiTi-3-45-Light', '', '/Users/admin/Downloads/AlibabaPuHuiTi-3/AlibabaPuHuiTi-3-45-Light/AlibabaPuHuiTi-3-45-Light.ttf', uni=True)  # 添加支持 Unicode 的字体
        pdf.set_font("AlibabaPuHuiTi-3-45-Light", size=12)  # 使用支持 Unicode 的字体

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img_path = f'temp_{page_num}.png'
            pix.save(img_path)

            # 使用OCR识别图像
            data = Sample.recognize_image(client, img_path)
            if 'content' in data:
                text = data['content']
                print(text)
            else:
                text = "No text recognized"

            # 写入PDF
            pdf.add_page()
            pdf.multi_cell(0, 10, txt=text)

            # 删除临时文件
            os.remove(img_path)

        # 保存PDF
        pdf.output(output_pdf_path)

    @staticmethod
    def main() -> None:

        input_pdf_path = "/Users/admin/Downloads/pdf/chanlun.pdf"
        output_txt_path = "/Users/admin/Downloads/pdf/chanlun_new.pdf"

        Sample.process_pdf(input_pdf_path, output_txt_path)


if __name__ == '__main__':
    Sample.main()
