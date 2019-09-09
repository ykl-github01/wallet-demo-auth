import HTMLTestReportCN
import case.creat_wallet
import case.getcoin
from case.asecretaddrtob_3tri import AsecretaaddrtoB_3TRI
from case.asecretaddramounttob_6rti import AsecretamounttoB_6TRI
from case.asecretamounttob_4tri import AsecretamounttoB_4TRI
from case.asunaddrtob_2rti import AsunaddrtoB_2TRI
from case.asecretaddrtob_7tri import AsecretaaddrtoB_7TRI
from case.asunaddrtob_5tri import AsunaddrtoB_5TRI
from case.getsecretcoin import GetSecretCoin
import unittest
import time
import os



class Walletprocess(unittest.TestCase):
        def setUp(self):
            pass
        def test_1creat_wallet(self):
            case.creat_wallet.CreatWallet().creat_wallet()
            print('创建钱包成功')
        def test_2getcoin(self):
            case.getcoin.GetCoin().getcoin()
            print('获取币成功')
        def test_3getsecretcoin(self):
            GetSecretCoin().getsecretcoin()
            print('获取隐私币成功')
        def test_4asunaddrtob_2tri(self):
            AsunaddrtoB_2TRI().asunaddrtob_2tri()
            print('A明文地址转B 2个TRI币成功')
        def test_5asecretaddrtob_3tri(self):
            AsecretaaddrtoB_3TRI().asecretaddrtob_3tri()
            print('A隐藏地址转B 3个TRI币成功')
        def test_6asecretamounttob_4tri(self):
            AsecretamounttoB_4TRI().asecretamounttob_4tri()
            print('A隐藏金额转B 4个TRI币成功')
        def test_7asunaddrtob_5tri(self):
            AsunaddrtoB_5TRI().asunaddrtob_5tri()
            print('A明文地址转B 5个TRI币成功')
        def test_8asecretaddramounttob_6rti(self):
            AsecretamounttoB_6TRI().asecretamounttob_6tri()
            print('A隐私地址隐私金额转B 6个TRI币成功')
        def test_9asecretaddrtob_7tri(self):
            AsecretaaddrtoB_7TRI().asecretaddrtob_7tri()
            print('A隐私地址转B 7个TRI币成功')
        def tearDown(self):
            pass



if __name__ == '__main__':
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    qian= os.path.abspath('.').split('process')[0]
    print(now_time)
    # 定义一个报告存放路径
    filename = qian+'report'+'\\'+ now_time + 'result.html'
    fp = open(filename, 'wb')

    testsuite=unittest.TestSuite()
    testsuite.addTest(Walletprocess('test_1creat_wallet'))
    testsuite.addTest(Walletprocess('test_2getcoin'))
    testsuite.addTest(Walletprocess('test_3getsecretcoin'))
    testsuite.addTest(Walletprocess('test_4asunaddrtob_2tri'))
    testsuite.addTest(Walletprocess('test_5asecretaddrtob_3tri'))
    testsuite.addTest(Walletprocess('test_6asecretamounttob_4tri'))
    testsuite.addTest(Walletprocess('test_7asunaddrtob_5tri'))
    testsuite.addTest(Walletprocess('test_8asecretaddramounttob_6rti'))
    testsuite.addTest(Walletprocess('test_9asecretaddrtob_7tri'))
    # 定义测试报告
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u'钱包流程用例',
        description=u"用例执行情况")

        # 运行测试用例
    runner.run(testsuite)

    fp.close()