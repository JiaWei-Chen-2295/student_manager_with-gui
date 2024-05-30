from NewStar.Dao.MajorDao import MajorDao
from NewStar.Objects.Major import Major

def add(major_name):
    """

    Args:
        major_name: 专业传参

    Returns:返回新增专业类

    """
    major = Major(major_name)
    md = MajorDao()
    md.insert(major)
def view_all_major():
    all_major = []
    md = MajorDao()
    major_list = md.selectAll()
    for i in major_list:
        a = {'id': i.major_id, 'major_name': i.major_name}
        all_major.append(a)
    return all_major

def viewSelf_major(major_id):
    major = []
    md = MajorDao()
    major_list = md.selectById(major_id)
    try:
        c = {'id': major_list.major_id, 'major_name':major_list.major_name}
        major.append(c)
        return major
    except:
        return None

def update(major_id,major_new_id,major_name):
    md = MajorDao()
    major_list = md.selectById(major_id)
    major_list.major_id = major_new_id
    major_list.major_name = major_name
    major_list = Major(major_list.major_id,major_list.major_name)
    return major_list

def delete(major_id):
    md = MajorDao()
    major_list = md.selectById(major_id)
    try:
        md.drop(major_list)
    except:
        return -1

if __name__ == '__main__':
    a = delete(5)

