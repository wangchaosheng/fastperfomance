from rest_framework.pagination import PageNumberPagination


# 重写PageNumberPagination父类，对分页进行拓展
from utils.respones import SUCCESS


class MyPagination(PageNumberPagination):
    # 指定默认每一页的数据条数
    page_size = 10
    # 设置前端指定页码的查询字符串key名称
    page_query_param = 'page'

    # 设置前端指定每一页数据条数的查询字符串key名称
    # 指定显示指定之后，前端才支持指定每一页的数据条数
    page_size_query_param = 'size'
    # 指定最大的每一页的数据条数
    max_page_size = 50
    page_query_description = '第几页'
    page_size_query_description = '每页几条'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_page_num'] = self.page.number
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data.update(SUCCESS)
        return response
