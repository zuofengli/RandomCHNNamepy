from random import Random


class RandomName:
    _first = [
        '王', '李', '张', '刘', '陈', '杨', '黄', '赵', '吴', '周', '徐', '孙', '马', '朱', '胡', '郭', '何', '高', '林', '罗', '郑', '梁',
        '谢', '宋', '唐', '许', '韩', '冯', '邓', '曹', '彭', '曾', '萧', '田', '董', '潘', '袁', '于', '蒋', '蔡', '余', '杜', '叶', '程',
        '苏', '魏', '吕', '丁', '任', '沈', '姚', '卢', '姜', '崔', '钟', '谭', '陆', '汪', '范', '金', '石', '廖', '贾', '夏', '韦', '傅',
        '方', '白', '邹', '孟', '熊', '秦', '邱', '江', '尹', '薛', '阎', '段', '雷', '侯', '龙', '史', '陶', '黎', '贺', '顾', '毛', '郝',
        '龚', '邵', '万', '钱', '严', '覃', '武', '戴', '莫', '孔', '向', '汤'
    ]
    _second70 = [
        '英', '华', '玉', '秀', '文', '明', '国', '春', '红', '丽', '小', '云', '平', '海', '珍', '荣'
    ]
    _second80 = [
        '一', '鹏', '涛', '杰', '健', '伟', '明', '晓', '春', '磊', ' ', ' ', ' ', ' ', ' '
    ]
    _second90 = [
        '英', '华', '玉', '秀', '文', '明', '国', '春', '红', '丽', '小', '云', '平', '海', '珍', '荣',
        '一', '鹏', '涛', '杰', '健', '伟', '明', '晓', '春', '磊', ' ', ' ', ' ', ' ', ' '
    ]
    _third70 = [
        '英', '华', '玉', '秀', '文', '明', '国', '春', '红', '丽', '小', '云', '平', '海', '珍', '荣'
    ]
    _third80 = [
        '一', '鹏', '涛', '杰', '健', '伟', '明', '晓', '春', '磊'
    ]
    _third90 = [
        '英', '华', '玉', '秀', '文', '明', '国', '春', '红', '丽', '小', '云', '平', '海', '珍', '荣',
        '一', '鹏', '涛', '杰', '健', '伟', '明', '晓', '春', '磊'
    ]

    def __init__(self, seed=None, first=None, second=None, third=None):
        if first is not None:
            self.first = first
        if second is not None:
            self.second = second
        if third is not None:
            self.third = third
        self.random = Random(seed)

    def randomname(self, age=70):
        first = self._random_element(self._first)
        second = ''
        third = ''
        if age == 70:
            second = self._random_element(self._second70)
            third = self._random_element(self._third70)
        if age == 80:
            second = self._random_element(self._second80)
            third = self._random_element(self._third80)
        if age == 90:
            second = self._random_element(self._second90)
            third = self._random_element(self._third90)
        sections = [first, second, third]
        return ''.join(str(i) for i in sections)

    def _random_element(self, s):
        if len(s) <= 0:
            return ''
        return self.random.choice(s)
