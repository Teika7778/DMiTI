from core.ABS_Z_N import ABS_Z_N
from core.ADD_1N_N import ADD_1N_N
from core.ADD_NN_N import ADD_NN_N
from core.ADD_PP_P import ADD_PP_P
from core.ADD_QQ_Q import ADD_QQ_Q
from core.ADD_ZZ_Z import ADD_ZZ_Z
from core.COM_NN_D import COM_NN_D
from core.DEG_P_N import DEG_P_N
from core.DER_P_P import DER_P_P
from core.DIV_NN_Dk import DIV_NN_Dk
from core.DIV_NN_N import DIV_NN_N
from core.DIV_PP_P import DIV_PP_P
from core.DIV_QQ_Q import DIV_QQ_Q
from core.DIV_ZZ_Z import DIV_ZZ_Z
from core.FAC_P_Q import FAC_P_Q
from core.GCF_NN_N import GCF_NN_N
from core.GCF_PP_P import GCF_PP_P
from core.INT_Q_B import INT_Q_B
from core.LCM_NN_N import LCM_NN_N
from core.LED_P_Q import LED_P_Q
from core.MOD_NN_N import MOD_NN_N
from core.MOD_PP_P import MOD_PP_P
from core.MOD_ZZ_Z import MOD_ZZ_Z
from core.MUL_ND_N import MUL_ND_N
from core.MUL_Nk_N import MUL_Nk_N
from core.MUL_NN_N import MUL_NN_N
from core.MOD_PP_P import MUL_PP_P
from core.MUL_PQ_P import MUL_PQ_P
from core.MUL_Pxk_P import MUL_Pxk_P
from core.MUL_QQ_Q import MUL_QQ_Q
from core.MUL_ZM_Z import MUL_ZM_Z
from core.MUL_ZZ_Z import MUL_ZZ_Z
from core.NMR_P_P import NMR_P_P
from core.NZER_N_B import NZER_N_B
from core.POZ_Z_D import POZ_Z_D
from core.RED_Q_Q import RED_Q_Q
from core.SUB_NDN_N import SUB_NDN_N
from core.SUB_NN_N import SUB_NN_N
from core.SUB_PP_P import SUB_PP_P
from core.SUB_QQ_Q import SUB_QQ_Q
from core.SUB_ZZ_Z import SUB_ZZ_Z
from core.TRANS_N_Z import TRANS_N_Z
from core.TRANS_Q_Z import TRANS_Q_Z
from core.TRANS_Z_N import TRANS_Z_N
from core.TRANS_Z_Q import TRANS_Z_Q


class ModuleNameParser:
    def __init__(self):
        self.names = dict()
        self.names["ABS_Z_N"] = ABS_Z_N()
        self.names["ADD_NN_N"] = ADD_NN_N()
        self.names["ADD_1N_N"] = ADD_1N_N()
        self.names["ADD_PP_P"] = ADD_PP_P()
        self.names["ADD_QQ_Q"] = ADD_QQ_Q()
        self.names["ADD_ZZ_Z"] = ADD_ZZ_Z()
        self.names["COM_NN_D"] = COM_NN_D()
        self.names["DEG_P_N"] = DEG_P_N()
        self.names["DER_P_P"] = DER_P_P()
        self.names["DIV_NN_Dk"] = DIV_NN_Dk()
        self.names["DIV_NN_N"] = DIV_NN_N()
        self.names["DIV_PP_P"] = DIV_PP_P()
        self.names["DIV_QQ_Q"] = DIV_QQ_Q()
        self.names["DIV_ZZ_Z"] = DIV_ZZ_Z()
        self.names["FAC_P_Q"] = FAC_P_Q()
        self.names["GCF_NN_N"] = GCF_NN_N()
        self.names["GCF_PP_P"] = GCF_PP_P()
        self.names["INT_Q_B"] = INT_Q_B()
        self.names["LCM_NN_N"] = LCM_NN_N()
        self.names["LED_P_Q"] = LED_P_Q()
        self.names["MOD_NN_N"] = MOD_NN_N()
        self.names["MOD_PP_P"] = MOD_PP_P()
        self.names["MOD_ZZ_Z"] = MOD_ZZ_Z()
        self.names["MUL_ND_N"] = MUL_ND_N()
        self.names["MUL_Nk_N"] = MUL_Nk_N()
        self.names["MUL_NN_N"] = MUL_NN_N()
        self.names["MUL_PP_P"] = MUL_PP_P()  # Исправлено: должно быть MUL_PP_P
        self.names["MUL_PQ_P"] = MUL_PQ_P()
        self.names["MUL_Pxk_P"] = MUL_Pxk_P()
        self.names["MUL_QQ_Q"] = MUL_QQ_Q()
        self.names["MUL_ZM_Z"] = MUL_ZM_Z()
        self.names["MUL_ZZ_Z"] = MUL_ZZ_Z()
        self.names["NMR_P_P"] = NMR_P_P()
        self.names["NZER_N_B"] = NZER_N_B()
        self.names["POZ_Z_D"] = POZ_Z_D()
        self.names["RED_Q_Q"] = RED_Q_Q()
        self.names["SUB_NDN_N"] = SUB_NDN_N()
        self.names["SUB_NN_N"] = SUB_NN_N()
        self.names["SUB_PP_P"] = SUB_PP_P()
        self.names["SUB_QQ_Q"] = SUB_QQ_Q()
        self.names["SUB_ZZ_Z"] = SUB_ZZ_Z()
        self.names["TRANS_N_Z"] = TRANS_N_Z()
        self.names["TRANS_Q_Z"] = TRANS_Q_Z()
        self.names["TRANS_Z_N"] = TRANS_Z_N()
        self.names["TRANS_Z_Q"] = TRANS_Z_Q()
        #дописать тут


    def parse(self, string):
        print(string)
        if string not in self.names:
            raise ValueError()
        return self.names[string]
