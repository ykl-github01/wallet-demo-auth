import HTMLTestReportCN
import case.creat_wallet
import case.getcoin
import unittest
import time


class Walletprocess(unittest.TestCase):
    def setUp(self):
        pass
    def test_creat_wallet(self):
        case.creat_wallet.CreatWallet().creat_wallet()
        print('创建钱包成功')
    def test_getcoin(self):
        case.getcoin.GetCoin().getcoin()
        print('获取币成功')
    def tearDown(self):
        pass



if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    print(now_time)
    # 定义一个报告存放路径
    filename = '../report/'+now_time+'result.html'
    fp = open(filename, 'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(Walletprocess('test_creat_wallet'))
    testsuite.addTest(Walletprocess('test_getcoin'))
    # 定义测试报告
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u'钱包流程用力',
        description=u"用例执行情况")

    # 运行测试用例
    runner.run(testsuite)

    fp.close()