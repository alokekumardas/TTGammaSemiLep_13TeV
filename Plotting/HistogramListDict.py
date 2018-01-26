btagWeightCategory = ["1","(1-btagWeight[0])","(btagWeight[2])","(btagWeight[1])"]


def GetHistogramInfo_2Dplot(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):
    histogramInfo = {"phosel_2DChIsoSIEIE_barrel":["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_barrel", [100,0,0.07], [100,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (abs(loosePhoSCEta)<1.47)"), "", True],
                     "phosel_2DChIsoSIEIE_endcap":["loosePhoPFChIso", "loosePhoSIEIE", "phosel_2DChIsoSIEIE_endcap", [100,0,0.07], [100,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (abs(loosePhoSCEta)>1.47)"), "", True],
                     "phosel_2DdRjetphoChIso":["dRPhotonJet[0]", "loosePhoPFChIso", "phosel_2DdRjetphoChIso", [200,0,5], [100,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"),"", True], 
                     }
    return histogramInfo

#def GetHistforfits(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):
#	histogramInfo ={"presel_M3_control"                     : ["M3"        , "presel_M3_control", [550,50,600],extraPhotonCuts%("nPho==0"), "", True],
#		      "phosel_noCut_ChIso"                  : ["loosePhoPFChIso" , "phosel_noCut_ChIso"                ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
 #                     "phosel_noCut_ChIso_GenuinePhoton"      : ["loosePhoPFChIso" , "phosel_noCut_ChIso_GenuinePhoton"  ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
 #                     "phosel_noCut_ChIso_MisIDEle"           : ["loosePhoPFChIso" , "phosel_noCut_ChIso_MisIDEle"       ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
  #                    "phosel_noCut_ChIso_HadronicPhoton"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicPhoton" ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
   #                   "phosel_noCut_ChIso_HadronicFake"       :["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicFake" ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],
#		      "phosel_M3"                             : ["M3"            , "phosel_M3"              ,    [550,50,600], extraPhotonCuts%("phoMediumID"), "", True],
 #                     "phosel_M3_GenuinePho"                  : ["M3"            , "phosel_M3_GenuinePho"   ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsGenuine")       , "", False],
  #                    "phosel_M3_MisIDEle"                    : ["M3"            , "phosel_M3_MisIDEle"     ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsMisIDEle")      , "", False],
   #                   "phosel_M3_HadronicPho"                 : ["M3"            , "phosel_M3_HadronicPho"  ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsHadronicPhoton"), "", False],
    #                  "phosel_M3_HadronicFake"                : ["M3"            , "phosel_M3_HadronicFake" ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsHadronicFake")  , "", False],
#		        "phosel_AntiSIEIE_ChIso"              : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso", [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],
#
#			"phosel_AntiSIEIE_ChIso_barrel"         : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_barrel" ,   [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE<0.055 && loosePhoSIEIE>0.015) && (abs(loosePhoSCEta)<1.47) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")   , "", True],
 #                    "phosel_AntiSIEIE_ChIso_endcap"                : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_endcap" ,   [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && (loosePhoSIEIE<0.055 && loosePhoSIEIE>0.031) && (abs(loosePhoSCEta)>1.47) && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")  , "", True],
#		  
#			}
#	return histogramInfo
			
def GetHistogramInfo(extraCuts="(passPresel_Mu && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Mu && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):

    histogramInfo = { "presel_jet1Pt"                         : ["jetPt[0]"  , "presel_jet1Pt"   ,    [1000,0,1000], extraCuts      , "", True],
                      "presel_jet2Pt"                         : ["jetPt[1]"  , "presel_jet2Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_jet3Pt"                         : ["jetPt[2]"  , "presel_jet3Pt"   ,      [600,0,600], extraCuts      , "", True],
                      "presel_Njet"                           : ["nJet"      , "presel_Njet"     ,        [15,0,15], extraCuts      , "", True],
                      "presel_Nbjet"                          : ["nBJet"     , "presel_Nbjet"    ,        [10,0,10], extraCuts      , "", True],
                      "presel_muPt"                           : ["muPt"      , "presel_muPt"     ,      [600,0,600], extraCuts      , "", True],
                      "presel_muEta"                          : ["muEta"     , "presel_muEta"    ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_muPhi"                          : ["muPhi"     , "presel_muPhi"    , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_elePt"                          : ["elePt"     , "presel_elePt"    ,      [600,0,600], extraCuts      , "", True],
                      "presel_eleSCEta"                       : ["eleSCEta"  , "presel_eleSCEta" ,   [100,-2.4,2.4], extraCuts      , "", True],
                      "presel_elePhi"                         : ["elePhi"    , "presel_elePhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_M3"                             : ["M3"        , "presel_M3"       ,     [550,50,600], extraCuts      , "", True],
                      "presel_M3_control"                     : ["M3"        , "presel_M3_control", [550,50,600],extraPhotonCuts%("nPho==0"), "", True],
                      "presel_MET"                            : ["pfMET"     , "presel_MET"      ,      [300,0,600], extraCuts      , "", True],
                      "presel_METPhi"                         : ["pfMETPhi"  , "presel_METPhi"   , [100,-3.15,3.15], extraCuts      , "", True],
                      "presel_nVtx"                           : ["nVtx"      , "presel_nVtx"     ,        [50,0,50], extraCuts      , "", True],
                      "presel_WtransMass"                     : ["WtransMass","presel_WtransMass",       [80,0,400], extraCuts      , "", True],
                      "presel_HT"                             : ["HT"        ,"presel_HT"        ,   [150,120,1500], extraCuts      , "", True],
                      "presel_nVtxup"                         : ["nVtx"      , "presel_nVtxup"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxdo"                         : ["nVtx"      , "presel_nVtxdo"   ,        [50,0,50], extraCuts      , "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "presel_nVtxNoPU"                       : ["nVtx"      , "presel_nVtxNoPU" ,        [50,0,50], extraCuts      , "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraCuts,btagWeightCategory[nBJets]), False],
                      "phosel_nVtxup"                         : ["nVtx"      , "phosel_nVtxup"   ,        [50,0,50], extraPhotonCuts%("phoMediumID"), "%sevtWeight*PUweight_Up*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("phoMediumID"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxdo"                         : ["nVtx"      , "phosel_nVtxdo"   ,        [50,0,50], extraPhotonCuts%("phoMediumID"), "%sevtWeight*PUweight_Do*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("phoMediumID"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtxNoPU"                       : ["nVtx"      , "phosel_nVtxNoPU" ,        [50,0,50], extraPhotonCuts%("phoMediumID"), "%sevtWeight*muEffWeight*eleEffWeight*%s"%(extraPhotonCuts%("phoMediumID"),btagWeightCategory[nBJets]), False],
                      "phosel_nVtx"                           : ["nVtx"      , "phosel_nVtx"     ,        [50,0,50], extraPhotonCuts%("phoMediumID") , "", True],
    #		  "phosel_DiphoMass"                      : ["DiphoMass"     , "phosel_DiphoMass"                     ,       [80,0,400], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_Nphotons"                       : ["nPho"          , "phosel_Nphotons"                      ,          [3,1,4], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_LeadingPhotonEt"                : ["phoEt[0]"      , "phosel_LeadingPhotonEt"               ,      [300,0,300], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_SecondLeadingPhotonEt"          : ["phoEt[1]"      , "phosel_SecondLeadingPhotonEt"         ,      [300,0,300], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_LeadingPhotonEta"               : ["phoEta[0]"     , "phosel_LeadingPhotonEta"              ,    [50,-2.5,2.5], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_LeadingPhotonSCEta"             : ["phoSCEta[0]"   , "phosel_LeadingPhotonSCEta"            ,    [50,-2.5,2.5], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_dRLeadingPhotonJet"             : ["dRPhotonJet[0]"   , "phosel_dRLeadingPhotonJet"            ,        [200,0,5], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_dRLeadingPromptPhotonJet"       : ["dRPhotonJet[0]"   , "phosel_dRLeadingPromptPhotonJet"      ,        [200,0,5], extraPhotonCuts%("phoMediumID && (photonIsGenuine||photonIsMisIDEle)"), "", False],
                      "phosel_dRLeadingNonPromptPhotonJet"    : ["dRPhotonJet[0]"   , "phosel_dRLeadingNonPromptPhotonJet"   ,        [200,0,5], extraPhotonCuts%("phoMediumID && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", False],
                      "phosel_dRLeadingPromptPhotonLepton"    : ["dRPhotonLepton[0]", "phosel_dRLeadingPromptPhotonLepton"   ,        [120,0,6], extraPhotonCuts%("phoMediumID && (photonIsGenuine||photonIsMisIDEle)"), "", False],
                      "phosel_dRLeadingNonPromptPhotonLepton" : ["dRPhotonLepton[0]", "phosel_dRLeadingNonPromptPhotonLepton",        [120,0,6], extraPhotonCuts%("phoMediumID && (photonIsHadronicPhoton||photonIsHadronicFake)"), "", False],
                      "phosel_dRLeadingGenuinePhotonLepton"   : ["dRPhotonLepton[0]", "phosel_dRLeadingGenuinePhotonLepton"  ,        [120,0,6], extraPhotonCuts%("phoMediumID && photonIsGenuine"),"", False],
                      "phosel_dRLeadingMisIDEleLepton"        : ["dRPhotonLepton[0]", "phosel_dRLeadingMisIDEleLepton"       ,        [120,0,6], extraPhotonCuts%("phoMediumID && photonIsMisIDEle"),"", False],
                      "phosel_dRLeadingHadPhoLepton"          : ["dRPhotonLepton[0]", "phosel_dRLeadingHadPhoLepton"         ,        [120,0,6], extraPhotonCuts%("phoMediumID && photonIsHadronicPhoton"),"", False],
                      "phosel_dRLeadingHadFakeLepton"         : ["dRPhotonLepton[0]", "phosel_dRLeadingHadFakeLepton"        ,        [120,0,6], extraPhotonCuts%("phoMediumID && photonIsHadronicFake"),"", False],
                      "phosel_dRLeadingPhotonLepton"          : ["dRPhotonLepton[0]", "phosel_dRLeadingPhotonLepton"         ,        [120,0,6], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_phoJetDR"                       : ["phoJetDR"         , "phosel_phoJetDR"                      ,        [200,0,5], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_WtransMass"                     : ["WtransMass"    , "phosel_WtransMass"      ,      [80,0,400], extraPhotonCuts%("phoMediumID"), "", True],		
                      "phosel_HT"                             : ["HT"            , "phosel_HT"              ,  [150,120,1500], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_M3"                             : ["M3"            , "phosel_M3"              ,    [550,50,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_M3_GenuinePho"                  : ["M3"            , "phosel_M3_GenuinePho"   ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsGenuine")       , "", False],
                      "phosel_M3_MisIDEle"                    : ["M3"            , "phosel_M3_MisIDEle"     ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsMisIDEle")      , "", False],
                      "phosel_M3_HadronicPho"                 : ["M3"            , "phosel_M3_HadronicPho"  ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsHadronicPhoton"), "", False],
                      "phosel_M3_HadronicFake"                : ["M3"            , "phosel_M3_HadronicFake" ,    [550,50,600], extraPhotonCuts%("phoMediumID && photonIsHadronicFake")  , "", False],
                      "phosel_MET"                            : ["pfMET"         , "phosel_MET"             ,    [550,50,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_elePt"                          : ["elePt"         , "phosel_elePt"           ,     [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_eleSCEta"                       : ["eleSCEta"      , "phosel_eleSCEta"        ,  [100,-2.4,2.4], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_muPt"                           : ["muPt"          , "phosel_muPt"            ,     [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_muEta"                          : ["muEta"         , "phosel_muEta"           ,  [100,-2.4,2.4], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_Njet"                           : ["nJet"          , "phosel_Njet"            ,       [15,0,15], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_Nbjet"                          : ["nBJet"         , "phosel_Nbjet"           ,       [10,0,10], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_HoverE"                         : ["phoHoverE"     , "phosel_HoverE"          ,    [100,0.,.04], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_SIEIE"                          : ["phoSIEIE"      , "phosel_SIEIE"           ,    [100,0.,.07], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_ChIso"                          : ["phoPFChIso"    , "phosel_ChIso"           ,      [100,0,.5], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_NeuIso"                         : ["phoPFNeuIso"   , "phosel_NeuIso"          ,      [100,0,5.], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_PhoIso"                         : ["phoPFPhoIso"   , "phosel_PhoIso"          ,        [50,0,5], extraPhotonCuts%("phoMediumID"), "", True],
                      ###############
                      "phosel_noCut_HoverE"                   : ["loosePhoHoverE"  , "phosel_noCut_HoverE"               ,      [100,0.,.2], extraPhotonCuts%("loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_SIEIE_barrel"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_barrel"         ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (abs(loosePhoSCEta)<1.47)"),"", True],
                      "phosel_noCut_SIEIE_endcap"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_endcap"         ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (abs(loosePhoSCEta)>1.47)"),"", True],
                      "phosel_noCut_SIEIE"                    : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE"                ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_SIEIE_GenuinePho"         : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_GenuinePho"     ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
                      "phosel_noCut_SIEIE_MisIDEle"           : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_MisIDEle"       ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
                      "phosel_noCut_SIEIE_HadPho"             : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadPho"         ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                      "phosel_noCut_SIEIE_HadFake"            : ["loosePhoSIEIE"   , "phosel_noCut_SIEIE_HadFake"        ,     [100,0.,.07], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],
                      "phosel_noCut_ChIso"                    : ["loosePhoPFChIso" , "phosel_noCut_ChIso"                ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso"), "", True],
                      "phosel_noCut_ChIso_GenuinePhoton"      : ["loosePhoPFChIso" , "phosel_noCut_ChIso_GenuinePhoton"  ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine"), "", False],
                      "phosel_noCut_ChIso_MisIDEle"           : ["loosePhoPFChIso" , "phosel_noCut_ChIso_MisIDEle"       ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle"), "", False],
                      "phosel_noCut_ChIso_HadronicPhoton"     : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicPhoton" ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                      "phosel_noCut_ChIso_HadronicFake"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_HadronicFake"   ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake"), "", False],
                      "phosel_noCut_ChIso_PromptPhoton"       : ["loosePhoPFChIso" , "phosel_noCut_ChIso_PromptPhoton"   ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (loosePhotonIsGenuine||loosePhotonIsMisIDEle)")           , "", False],
                      "phosel_noCut_ChIso_NonPromptPhoton"    : ["loosePhoPFChIso" , "phosel_noCut_ChIso_NonPromptPhoton",        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && (loosePhotonIsHadronicPhoton||loosePhotonIsHadronicFake)"), "", False],
                      "phosel_noCut_NeuIso"                   : ["loosePhoPFNeuIso", "phosel_noCut_NeuIso"               ,        [80,0,40], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassPhoIso")                                 , "", True],
                      "phosel_noCut_PhoIso"                   : ["loosePhoPFPhoIso", "phosel_noCut_PhoIso"               ,      [200,0,100], extraPhotonCuts%("loosePhoMediumIDPassHoverE && loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassChIso && loosePhoMediumIDPassNeuIso")                                 , "", True],
                      "phosel_AntiSIEIE_ChIso"                : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso"            ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso")                               , "", True],
                      "phosel_AntiSIEIE_ChIso_GenuinePho"     : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_GenuinePho" ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsGenuine")       , "", False],
                      "phosel_AntiSIEIE_ChIso_MisIDEle"       : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_MisIDEle"   ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsMisIDEle")      , "", False],
                      "phosel_AntiSIEIE_ChIso_HadPho"         : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadPho"     ,        [80,0,20], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicPhoton"), "", False],
                      "phosel_AntiSIEIE_ChIso_HadFake"        : ["loosePhoPFChIso" , "phosel_AntiSIEIE_ChIso_HadFake"    ,       [200,0,50], extraPhotonCuts%("loosePhoMediumIDPassHoverE && !loosePhoMediumIDPassSIEIE && loosePhoMediumIDPassNeuIso && loosePhoMediumIDPassPhoIso && loosePhotonIsHadronicFake")  , "", False],
                      #################
                      "phosel_NGenuinePho"                    : ["nPho"              , "phosel_NGenuinePho"       ,          [2,0,2], extraPhotonCuts%("photonIsGenuine")                       , "", False],
                      "phosel_NMisIDEle"                      : ["nPho"              , "phosel_NMisIDEle"         ,          [2,0,2], extraPhotonCuts%("photonIsMisIDEle")                      , "", False],
                      "phosel_NHadronicPho"                   : ["nPho"              , "phosel_NHadronicPho"      ,          [2,0,2], extraPhotonCuts%("photonIsHadronicPhoton")                , "", False],
                      "phosel_NHadronicFake"                  : ["nPho"              , "phosel_NHadronicFake"     ,          [2,0,2], extraPhotonCuts%("photonIsHadronicFake")                  , "", False],
                      "phosel_RandomCone"                     : ["phoPFRandConeChIso", "phosel_RandomCone"        ,        [80,0,20], extraPhotonCuts%("phoMediumID")                           , "", False],
                      "phosel_RandomConeJetDR"                : ["phoPFRandConeJetDR", "phosel_RandomConeJetDR"   ,        [200,0,5], extraPhotonCuts%("phoMediumID")                           , "", False],
                      "phosel_mcMomPIDGenuinePho"             : ["photonParentPID"   , "phosel_mcMomPIDGenuinePho",[2000,-1000,1000], extraPhotonCuts%("phoMediumID && photonIsGenuine")        , "", False],
                      "phosel_mcMomPIDMisIDEle"               : ["photonParentPID"   , "phosel_mcMomPIDMisIDEle"  ,[2000,-1000,1000], extraPhotonCuts%("phoMediumID && photonIsMisIDEle")       , "", False],
                      "phosel_mcMomPIDHadPho"                 : ["photonParentPID"   , "phosel_mcMomPIDHadPho"    ,[2000,-1000,1000], extraPhotonCuts%("phoMediumID && photonIsHadronicPhoton") , "", False],
                      "phosel_mcMomPIDHadFake"                : ["photonParentPID"   , "phosel_mcMomPIDHadFake"   ,[2000,-1000,1000], extraPhotonCuts%("phoMediumID && photonIsHadronicFake")   , "", False],
                      "phosel_PhotonCategory"                 : ["photonIsGenuine[0] + 2*photonIsMisIDEle[0] + 3*photonIsHadronicPhoton[0] + 4*photonIsHadronicFake[0]", "phosel_PhotonCategory", [4,1,5], extraPhotonCuts%("phoMediumID"), "", False],
                      ################
                      "phosel_MassEGamma"                     : ["phoMassEGamma", "phosel_MassEGamma", [200,0,200], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_Mt_blgammaMET"                  : ["Mt_blgammaMET" , "phosel_Mt_blgammaMET" , [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_Mt_lgammaMET"                   : ["Mt_lgammaMET"  , "phosel_Mt_lgammaMET"  , [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_M_bjj"                          : ["M_bjj"         , "phosel_M_bjj"         , [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_M_jj"                           : ["M_jj"          , "phosel_M_jj"          , [600,0,600], extraPhotonCuts%("phoMediumID"), "", True],
                      "phosel_MassCuts"                       : ["MassCuts"      , "phosel_MassCuts"      , [2,0,2], extraPhotonCuts%("phoMediumID"), "", True],                  
                      "presel_DilepMass"                      : ["DilepMass"     , "presel_DilepMass"     , [300,0,300],extraCuts,"",True],
                      "presel_DilepDR"                      : ["DilepDelR"     , "presel_DilepDR"       , [100,0,6],extraCuts,"",True],
                      "phosel_DilepMass"                      : ["DilepMass"     , "phosel_DilepMass"     , [300,0,300],extraPhotonCuts%("phoMediumID"),"",True],
                      "phosel_DilepDR"                      : ["DilepDelR"     , "phosel_DilepDR"       , [100,0,6]  ,extraPhotonCuts%("phoMediumID"),"",True],
                      }
    return histogramInfo

#def GetHistforZGamma(extraCuts="(passPresel_Ele && nJet>=3 && nBJet>=1)*", extraPhotonCuts="(passPresel_Ele && nJet>=3 && nBJet>=1 && %s)*", nBJets=1):
#	 histogramInfo = { "phosel_MassEGamma"                     : ["phoMassEGamma", "phosel_MassEGamma", [200,0,200], extraPhotonCuts%("phoMediumID"), "", True],
#		    	   "phosel_MassEGammaMisIDEle"             : ["phoMassEGamma", "phosel_MassEGammaMisIDEle", [200,0,200], extraPhotonCuts%("phoMediumID && photonIsMisIDEle"), "", True],
#			   "phosel_MassEGammaOthers"               : ["phoMassEGamma", "phosel_MassEGammaOthers", [200,0,200], extraPhotonCuts%("phoMediumID && (photonIsGenuine||photonIsHadronicFake||photonIsHadronicPhoton)"), "", True]
 #                        }
#	 return  histogramInfo
