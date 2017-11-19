import pandas as pd
import datetime

ogdf = pd.read_csv("Health-Nutrition-and-Population.csv")

list1 = [i for i in range(0, 14145)]

ogdf.drop(ogdf.index[list1], inplace=True)
ogdf = ogdf[['Country Code', 'Indicator Name', 'Indicator Code', '2010', '2011', '2012', '2013', '2014', '2015']]

list1 = ogdf['Indicator Code'].tolist()

##Using a dictionary of frequency of metrics, we remove metrics where more than half the data is missing
dict = {'SP.POP.AG19.FE.IN': 1166, 'SP.POP.AG06.MA.IN': 1166, 'SP.POP.AG08.MA.IN': 1166, 'SP.RUR.TOTL': 1232, 'SH.HIV.1524.KW.FE.ZS': 127, 'SP.POP.4044.FE': 1160, 'SP.POP.6064.MA': 1160, 'SP.POP.65UP.TO': 1162, 'SP.POP.3539.FE.5Y': 1160, 'SP.POP.5559.MA': 1160, 'SH.HIV.ARTC.ZS': 618, 'SE.PRM.CMPT.FE.ZS': 604, 'SP.POP.6064.FE.5Y': 1160, 'SP.POP.AG18.FE.IN': 1166, 'SP.POP.4044.FE.5Y': 1160, 'SP.DYN.CBRT.IN': 1022, 'SP.POP.AG00.MA.IN': 1166, 'SH.DTH.NMRT': 1150, 'SH.DTH.COMM.ZS': 172, 'SH.HIV.INCD.TL': 642, 'SP.POP.AG05.FE.IN': 1166, 'SH.STA.ARIC.ZS': 127, 'SH.DYN.AIDS.ZS': 636, 'SH.ANM.ALLW.ZS': 378, 'SH.MMR.RISK': 1098, 'SP.POP.AG07.MA.IN': 1166, 'SH.MMR.WAGE.ZS': 447, 'SP.DYN.CONU.ZS': 165, 'SE.ADT.LITR.ZS': 368, 'SH.TBS.MORT': 1023, 'SP.POP.7579.MA.5Y': 1160, 'SH.XPD.TOTL.CD': 948, 'SP.POP.AG02.FE.IN': 1166, 'SH.STA.ODFC.UR.ZS': 630, 'SH.TBS.DTEC.ZS': 1006, 'SP.POP.65UP.FE.IN': 1162, 'SP.DYN.TO65.MA.ZS': 970, 'SE.SEC.NENR.FE': 446, 'SP.POP.AG11.FE.IN': 1166, 'SP.POP.3034.MA': 1160, 'SP.POP.AG14.MA.IN': 1166, 'SE.SEC.ENRR': 687, 'SH.STA.ORTH': 122, 'SP.UWT.TFRT': 115, 'SH.STA.ORCF.ZS': 119, 'SE.SEC.NENR.MA': 446, 'SH.XPD.TOTL.ZS': 948, 'SL.UEM.TOTL.ZS': 870, 'SP.POP.5054.FE': 1160, 'SH.PRG.ANEM': 370, 'SH.STA.STNT.FE.ZS': 112, 'SP.POP.3034.FE.5Y': 1160, 'SP.POP.1564.MA.IN': 1162, 'SH.MLR.SPF2.ZS': 60, 'SH.HIV.0014': 594, 'SP.HOU.FEMA.ZS': 66, 'SH.MMR.DTHS': 1086, 'SP.POP.AG20.FE.IN': 1166, 'SP.DYN.IMRT.IN': 1158, 'SH.CON.AIDS.FE.ZS': 46, 'SP.POP.0509.MA.5Y': 1160, 'SH.XPD.PCAP.PP.KD': 948, 'SH.TBS.PREV': 1047, 'SP.POP.6569.FE.5Y': 1160, 'SP.POP.AG15.MA.IN': 1166, 'SE.TER.ENRR.FE': 610, 'SH.HIV.1524.MA.ZS': 636, 'SH.STA.OWGH.MA.ZS': 110, 'SP.POP.AG21.FE.IN': 1166, 'SH.STA.MALN.MA.ZS': 114, 'SH.STA.OW15.ZS': 380, 'SP.POP.3539.MA': 1160, 'SP.POP.6569.FE': 1160, 'SH.PRG.SYPH.ZS': 264, 'SH.DTH.NCOM.ZS': 172, 'SH.STA.MALR': 437, 'SP.POP.0014.FE.IN': 1162, 'SP.POP.AG13.FE.IN': 1166, 'SH.STA.ODFC.ZS': 754, 'SP.POP.AG23.MA.IN': 1166, 'SE.PRM.NENR': 612, 'SE.PRM.NENR.MA': 548, 'SP.POP.AG02.MA.IN': 1166, 'SE.ADT.LITR.MA.ZS': 368, 'SP.POP.0004.FE': 1160, 'SH.XPD.OOPC.ZS': 948, 'SP.POP.AG10.FE.IN': 1166, 'SP.DYN.LE00.FE.IN': 998, 'SP.POP.AG16.MA.IN': 1166, 'SP.POP.7579.FE': 1160, 'SP.REG.BRTH.ZS': 223, 'SE.PRM.NENR.FE': 548, 'SP.POP.7074.FE.5Y': 1160, 'SN.ITK.VITA.ZS': 295, 'SP.POP.AG13.MA.IN': 1166, 'SP.ADO.TFRT': 970, 'SP.POP.65UP.MA.IN': 1162, 'SP.DYN.TFRT.IN': 1004, 'SH.XPD.PCAP': 948, 'SP.POP.AG12.MA.IN': 1166, 'SH.CON.AIDS.MA.ZS': 43, 'SP.POP.5559.FE.5Y': 1160, 'SH.STA.ACSN': 1167, 'SN.ITK.DEFC.ZS': 690, 'SP.POP.7579.FE.5Y': 1160, 'SH.ANM.CHLD.ZS': 370, 'SP.POP.7579.MA': 1160, 'SH.PRV.SMOK.MA': 252, 'SH.XPD.EXTR.ZS': 700, 'SN.ITK.SALT.ZS': 56, 'SP.POP.7074.MA.5Y': 1160, 'SP.POP.2529.MA.5Y': 1160, 'SP.RUR.TOTL.ZS': 1232, 'SP.POP.2529.MA': 1160, 'SP.POP.2529.FE.5Y': 1160, 'NY.GNP.PCAP.CD': 1106, 'SL.UEM.TOTL.FE.ZS': 870, 'SL.TLF.TOTL.IN': 927, 'SH.HIV.INCD.14': 594, 'SP.POP.6569.MA': 1160, 'SH.CON.1524.MA.ZS': 36, 'SH.MED.NUMW.P3': 300, 'SP.POP.TOTL': 1298, 'SP.POP.AG20.MA.IN': 1166, 'SH.IMM.IBCG': 938, 'SH.XPD.PRIV.ZS': 948, 'SH.STA.PNVC.ZS': 55, 'SP.POP.1519.FE.5Y': 1160, 'SH.STA.OWGH.FE.ZS': 108, 'SH.DYN.MORT': 1158, 'SE.PRM.CMPT.MA.ZS': 604, 'SP.POP.80UP.MA.5Y': 1160, 'SP.POP.AG15.FE.IN': 1166, 'SP.POP.3539.MA.5Y': 1160, 'SH.SVR.WAST.MA.ZS': 106, 'SH.HIV.KNOW.FE.ZS': 106, 'SE.ADT.1524.LT.MA.ZS': 364, 'SP.POP.AG17.FE.IN': 1166, 'SH.STA.ACSN.RU': 1143, 'SP.REG.BRTH.UR.ZS': 118, 'SP.POP.2024.MA.5Y': 1160, 'SE.ADT.1524.LT.ZS': 367, 'SH.TBS.INCD': 1047, 'SH.H2O.SAFE.RU.ZS': 1139, 'SE.ENR.ORPH': 68, 'SH.DYN.MORT.MA': 386, 'SE.XPD.TOTL.GD.ZS': 446, 'SP.POP.AG18.MA.IN': 1166, 'SP.MTR.1519.ZS': 64, 'SP.URB.TOTL': 1286, 'SH.STA.ODFC.RU.ZS': 734, 'SP.POP.3539.FE': 1160, 'SP.POP.4044.MA': 1160, 'SL.EMP.INSV.FE.ZS': 399, 'SP.POP.5054.MA': 1160, 'SH.DTH.INJR.ZS': 172, 'SE.ADT.1524.LT.FM.ZS': 364, 'SE.SEC.NENR': 487, 'SH.STA.WAST.ZS': 132, 'SP.DYN.WFRT': 52, 'SH.MMR.LEVE': 448, 'SH.DTH.IMRT': 1157, 'SH.IMM.MEAS': 1151, 'SE.TER.ENRR': 625, 'SH.SVR.WAST.FE.ZS': 104, 'SH.STA.MMRT.NE': 202, 'SP.POP.AG24.MA.IN': 1166, 'SP.POP.5054.FE.5Y': 1160, 'SH.SVR.WAST.ZS': 124, 'SP.DYN.SMAM.FE': 248, 'SP.RUR.TOTL.ZG': 787, 'SH.HIV.1524.FE.ZS': 636, 'SH.SGR.CRSK.ZS': 185, 'SP.POP.1014.FE': 1160, 'SH.STA.STNT.MA.ZS': 114, 'SP.REG.BRTH.RU.ZS': 118, 'SH.IMM.IDPT': 1151, 'SH.H2O.SAFE.ZS': 1163, 'SP.POP.AG06.FE.IN': 1166, 'SH.ANM.NPRG.ZS': 370, 'SP.POP.AG11.MA.IN': 1166, 'SP.POP.0509.FE.5Y': 1160, 'SH.DYN.AIDS': 642, 'SP.REG.DTHS.ZS': 124, 'SP.POP.1564.TO': 1162, 'SH.IMM.HIB3': 1068, 'SP.POP.DPND': 1162, 'SP.POP.TOTL.MA.IN': 1162, 'SP.POP.AG03.MA.IN': 1166, 'SH.STA.DIAB.ZS': 208, 'SP.POP.AG09.MA.IN': 1166, 'SH.XPD.PUBL.GX.ZS': 948, 'SP.POP.6064.FE': 1160, 'SP.DYN.SMAM.MA': 217, 'SH.IMM.HEPB': 1081, 'SP.POP.0509.MA': 1160, 'SP.POP.7074.FE': 1160, 'SH.HIV.KNOW.MA.ZS': 68, 'SH.STA.WAST.FE.ZS': 112, 'SP.POP.3034.FE': 1160, 'SH.DYN.MORT.FE': 386, 'SP.POP.AG03.FE.IN': 1166, 'SH.MLR.TRET.ZS': 83, 'SP.POP.1564.FE.IN': 1162, 'SP.DYN.AMRT.FE': 884, 'SP.POP.1014.FE.5Y': 1160, 'SP.POP.4549.MA': 1160, 'SH.PRV.SMOK.FE': 256, 'SH.MED.SAOP.P5': 171, 'SH.HIV.PMTC.ZS': 590, 'SH.STA.OWGH.ZS': 130, 'SH.VAC.TTNS.ZS': 635, 'SH.HIV.1524.KW.MA.ZS': 84, 'SP.POP.1519.MA': 1160, 'SI.POV.URHC': 163, 'SH.HIV.INCD': 642, 'SH.STA.OW15.MA.ZS': 380, 'SP.POP.AG01.MA.IN': 1166, 'SP.POP.AG22.MA.IN': 1166, 'SP.POP.AG21.MA.IN': 1166, 'SP.POP.0004.MA': 1160, 'SP.POP.TOTL.MA.ZS': 1162, 'SH.STA.IYCF.ZS': 64, 'SP.POP.AG01.FE.IN': 1166, 'SP.POP.DPND.OL': 1162, 'SP.POP.1564.MA.ZS': 1162, 'SH.CON.1524.FE.ZS': 41, 'SE.PRM.ENRR': 755, 'SH.HIV.TOTL': 642, 'SP.POP.0014.TO.ZS': 1162, 'SP.DYN.IMRT.FE.IN': 386, 'SP.URB.TOTL.IN.ZS': 1286, 'SP.POP.AG24.FE.IN': 1166, 'SH.XPD.PUBL': 948, 'SP.POP.65UP.TO.ZS': 1162, 'SH.STA.OW15.FE.ZS': 380, 'SH.XPD.PRIV': 948, 'SP.POP.AG23.FE.IN': 1166, 'SI.POV.RUHC': 162, 'SP.POP.1519.FE': 1160, 'SP.DYN.IMRT.MA.IN': 386, 'SP.DYN.LE00.MA.IN': 998, 'SH.DTH.MORT': 1158, 'SP.POP.AG05.MA.IN': 1166, 'SH.STA.MALN.FE.ZS': 112, 'SH.STA.ACSN.UR': 1169, 'SP.POP.0014.MA.ZS': 1162, 'SP.POP.AG25.FE.IN': 1166, 'SH.MED.BEDS.ZS': 264, 'SH.MED.PHYS.ZS': 325, 'SP.POP.4549.FE.5Y': 1160, 'SH.STA.ANVC.ZS': 159, 'SP.POP.AG14.FE.IN': 1166, 'SP.POP.5559.MA.5Y': 1160, 'SP.POP.BRTH.MF': 970, 'SP.POP.1519.MA.5Y': 1160, 'SH.DYN.AIDS.DH': 642, 'SH.STA.MMRT': 1098, 'SP.POP.2024.FE': 1160, 'SL.UEM.TOTL.MA.ZS': 870, 'SN.ITK.DEFC': 497, 'SP.POP.0014.MA.IN': 1162, 'SH.STA.BRTW.ZS': 137, 'SP.POP.AG22.FE.IN': 1166, 'SH.SGR.IRSK.ZS': 178, 'SE.SEC.ENRR.FE': 671, 'SE.SEC.ENRR.MA': 671, 'SH.STA.MALN.ZS': 132, 'SH.H2O.SAFE.UR.ZS': 1179, 'SP.POP.5054.MA.5Y': 1160, 'SP.POP.4044.MA.5Y': 1160, 'SP.DYN.LE00.IN': 998, 'SP.POP.AG16.FE.IN': 1166, 'SH.IMM.POL3': 1151, 'SH.XPD.PUBL.ZS': 948, 'SP.POP.1014.MA': 1160, 'SH.MLR.NETS.ZS': 78, 'SP.DYN.AMRT.MA': 884, 'SH.MLR.PREG.ZS': 27, 'SP.POP.AG19.MA.IN': 1166, 'SP.POP.AG10.MA.IN': 1166, 'SP.POP.0004.FE.5Y': 1160, 'SP.POP.0004.MA.5Y': 1160, 'SP.POP.5559.FE': 1160, 'SI.POV.NAHC': 249, 'SP.POP.0014.FE.ZS': 1162, 'SH.TBS.CURE.ZS': 762, 'SP.POP.1014.MA.5Y': 1160, 'SP.POP.1564.FE.ZS': 1162, 'SH.MED.CMHW.P3': 17, 'SP.POP.2529.FE': 1160, 'SH.STA.ANV4.ZS': 151, 'SH.STA.BFED.ZS': 143, 'SP.POP.TOTL.FE.ZS': 1162, 'SP.POP.80UP.MA': 1160, 'SP.POP.1564.TO.ZS': 1162, 'SH.DYN.AIDS.FE.ZS': 636, 'SP.POP.2024.FE.5Y': 1160, 'SP.DYN.TO65.FE.ZS': 970, 'SH.SGR.PROC.P5': 184, 'SP.POP.GROW': 1135, 'SE.PRM.CMPT.ZS': 625, 'SP.POP.AG04.MA.IN': 1166, 'SP.POP.AG25.MA.IN': 1166, 'SP.POP.80UP.FE.5Y': 1160, 'SP.POP.65UP.FE.ZS': 1162, 'SH.MMR.RISK.ZS': 1098, 'SP.POP.AG17.MA.IN': 1166, 'SH.STA.BRTC.ZS': 230, 'SP.POP.80UP.FE': 1160, 'SH.XPD.OOPC.TO.ZS': 948, 'SP.POP.DPND.YG': 1162, 'SE.PRM.ENRR.FE': 744, 'SH.STA.TRAF.P5': 178, 'SH.STA.STNT.ZS': 132, 'SH.HIV.ORPH': 588, 'SP.POP.65UP.MA.ZS': 1162, 'SH.FPL.SATI.ZS': 50, 'SP.URB.GROW': 1136, 'SP.POP.AG08.FE.IN': 1166, 'SP.POP.AG07.FE.IN': 1166, 'SL.TLF.TOTL.FE.ZS': 927, 'SP.DYN.CDRT.IN': 1021, 'SH.FPL.SATM.ZS': 52, 'SP.POP.7074.MA': 1160, 'SP.POP.3034.MA.5Y': 1160, 'SP.POP.6064.MA.5Y': 1160, 'SP.DYN.CONM.ZS': 128, 'SP.POP.TOTL.FE.IN': 1162, 'SP.POP.0509.FE': 1160, 'SH.DYN.NMRT': 1158, 'SP.POP.AG00.FE.IN': 1166, 'SP.POP.4549.FE': 1160, 'SM.POP.NETM': 72, 'SP.POP.4549.MA.5Y': 1160, 'SH.STA.WAST.MA.ZS': 114, 'SP.POP.AG09.FE.IN': 1166, 'SE.ADT.LITR.FE.ZS': 368, 'SH.HIV.INCD.ZS': 642, 'SP.POP.2024.MA': 1160, 'SP.POP.AG04.FE.IN': 1166, 'SP.POP.6569.MA.5Y': 1160, 'SP.POP.AG12.FE.IN': 1166, 'SE.PRM.ENRR.MA': 744, 'SP.POP.0014.TO': 1162}
dict_updated={}
dict_updated_withoutpop = {}
for key in dict.keys():
    if dict[key] >= 651:
         dict_updated[key]= dict[key]
         

##Using the previously obtained dictionary, remove all population metrics
for key in dict_updated.keys():
    if key.find("POP") == -1:
        dict_updated_withoutpop[key] = dict_updated[key]
        
##Change the dataframe to only include the desired metrics present in the updated without population dictionary
for key in dict_updated_withoutpop.keys():
    ogdf = ogdf[ogdf.Indicator_Code == key]
ogdf = ogdf[ogdf['Indicator_Code'].isin(list(dict_updated_withoutpop.keys()))]

for index,row in ogdf.iterrows():
    if row['Indicator Code'] not in dict_updated_withoutpop.keys():
        ogdf.drop(ogdf.index[index], inplace=True)


##We remove metrics that are very similar to already existing ones, s.t. to make the end product user friendly
code_delete = []
for i in range(0,71):
    if ogdf.iloc[i]['Status'] == 'D':
        code_delete.append(ogdf.iloc[i]['Indicator_Code'])

ogdf = ogdf[~ogdf['Indicator_Code'].isin(code_delete)]


##We keep a list of metrics that are inversely proportional to developement. Since metrics are either inversely proportional or not, all metrics
## not in the list are not inversely proportional. This will be used later on.
inverse=[]
for i in range(0,71):
        if ogdf1.iloc[i]['Status'] == 'I':
            inverse.append(ogdf1.iloc[i]['Indicator_Code'])

ogdf.sort_values('Indicator_Code', inplace = True)


##This normalizes all the data by finding the maximum value of a given year and metric, and then deividing all values by the maximum to yield something
## between 0 and 1. If metrics are to be inverted, that is done prior. 
for i in range (0,47):
    invert = False
    if ogdf.iloc[i*214]['Indicator_Code'] in inverse:
        invert = True
    for j in range(2010,2016):
        if invert == True:
            for k in range(0,214):
                if float(ogdf.iloc[k+214*i][str(j)]) != 0:
                    ogdf.at[ogdf.index[k + 214*i],str(j)] = 1/float(ogdf.iloc[k+214*i][str(j)])
        maximum = 0
        for k in range(0,214):
            if maximum < ogdf.iloc[k+214*i][str(j)]:
                maximum = ogdf.iloc[k+214*i][str(j)]
        if maximum == 0:
            for k in range(0,214):
                ogdf.at[ogdf.index[k + 214*i],str(j)] = 0
        else:
            for k in range(0,214):
                ogdf.at[ogdf.index[k + 214*i],str(j)] = float(ogdf.iloc[k+214*i][str(j)])/ float(maximum)

##ogdf.to_csv("edited52.csv")
