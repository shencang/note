import json

import xlwt


# 解析json
def read_json_file():
    js_object = json.load(open(r'ud.txt', encoding='utf-8'))
    return js_object


# 转换为excel
def json_2_excel():
    json_file = read_json_file()
    workbook = xlwt.Workbook()
    sheet1 = excel_title(workbook)
    print(len(json_file))
    # 第一层循环，依次取出区位字典，t代表区位号
    for t in range(0, len(json_file)):
        topic = json_file[t]
        # 课题名称
        topic_name = topic["topicName"]
        sheet1.write(t + 1, 0, topic_name)
        # 课题教师详细信息
        base_user_info = topic["baseUserInfo"]
        teacher_name = base_user_info["userName"]
        sheet1.write(t + 1, 1, teacher_name)
        teacher_num = base_user_info["userAccount"]
        sheet1.write(t + 1, 2, teacher_num)
        teacher_pwd = base_user_info["userPwd"]
        sheet1.write(t + 1, 3, teacher_pwd)
        # 课题描述
        topic_synopsis = topic["synopsis"]
        sheet1.write(t + 1, 4, topic_synopsis)
        # 课题要求
        topic_requirement = topic["requirement"]
        sheet1.write(t + 1, 5, topic_requirement)
        # 课题是否是新题
        topic_is_renewal = topic["isRenewal"]
        sheet1.write(t + 1, 6, topic_is_renewal)
        # 课题时间
        topic_time = topic["topicTime"]
        sheet1.write(t + 1, 7, topic_time)
        # 课题时间
        topic_property = topic["topicProperty"]
        sheet1.write(t + 1, 8, topic_property)

    workbook.save("Graduation_design_topics.xls")


def excel_title(workbook):
    sheet1 = workbook.add_sheet('毕设教师题目表', cell_overwrite_ok=True)
    style0 = xlwt.easyxf('font: name 黑体, color-index black, bold on',
                         num_format_str='#,##0.00')
    sheet1.write(0, 0, '课题名称', style0)
    sheet1.write(0, 1, '教师', style0)
    sheet1.write(0, 2, '工号', style0)
    sheet1.write(0, 3, '密钥', style0)
    sheet1.write(0, 4, '课题描述', style0)
    sheet1.write(0, 5, '课题要求', style0)
    sheet1.write(0, 6, '是否为新课题', style0)
    sheet1.write(0, 7, '课题时间', style0)
    sheet1.write(0, 8, '课题主题', style0)
    sheet1.col(0).width = 15000
    sheet1.col(1).width = 2000
    sheet1.col(2).width = 3000
    sheet1.col(3).width = 8500
    sheet1.col(4).width = 65535
    sheet1.col(5).width = 65535
    sheet1.col(6).width = 3000
    sheet1.col(7).width = 3000
    sheet1.col(8).width = 5000
    return sheet1


json_2_excel()
