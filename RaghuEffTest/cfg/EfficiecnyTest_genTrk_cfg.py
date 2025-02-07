import FWCore.ParameterSet.Config as cms

process = cms.Process("RaghuEffTest")

process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('MergingProducer.generalAndHiPixelTracks.MergingPixAndGenProducer_cfi')

# __________________ General _________________

# Configure the logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
)

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(3000) 
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(

                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_1.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_2.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_3.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_4.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_5.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_6.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_7.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_8.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_9.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_10.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_11.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_12.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_14.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_15.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_16.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_17.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_18.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_19.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_20.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_MINIAOD_v5/231024_131749/0000/miniaod_21.root',
                            
      
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_1.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_10.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_100.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_101.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_102.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_103.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_104.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_105.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_106.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_107.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_108.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_109.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_110.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_111.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_112.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_113.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_114.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_115.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_116.root',
                                #'/store/user/sarteaga/MinBias_PbPb_5p36TeV_Hydjet_v1/MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5/231023_223729/0000/stepRECO_117.root'

                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_1.root',
                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_2.root',
                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_3.root',
                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_4.root',
                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_5.root',
                                '/store/user/cbennett/PYTHIA8_HYDJET_DiJet_5360GeV_130X/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_updatedEra_132X_2024-10-12/241013_021405/0000/PYTHIA8_HYDJET_DiJet_5360GeV_RECODEBUG_6.root',
                                
                                #'file:/eos/cms/store/group/phys_heavyions/soohwan/samples/HLTTracking/step3AOD_py_REPACK_RAW2DIGI_L1Reco_RECO.root',
                            ),
                            duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
                            skipBadFiles=cms.untracked.bool(True)
)


##json
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '/eos/cms/store/group/phys_heavyions/sayan/HIN_run3_pseudo_JSON/HIPhysicsRawPrime/Golden_Online_live.json').getVLuminosityBlockRange()

### centrality ###
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

# Set the global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '132X_mcRun3_2023_realistic_HI_v5', '')
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
             tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_Nominal"),
             connect = cms.string("sqlite_file:CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_Nominal.db"),
             label = cms.untracked.string("HFtowers")
    ),
])


# __________________ Event selection _________________
# Add PbPb collision event selection

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')


# Define the event selection sequence
process.eventFilter = cms.Sequence(
    process.phfCoincFilter2Th4 *
    process.primaryVertexFilter *
    process.clusterCompatibilityFilter
)


# Define the output
process.TFileService = cms.Service("TFileService",fileName = cms.string('Eff_test_noChi2_nhits0_pTResoCutgt10GeV_RECODEBUG_QCDSample.root'))

###trigger selection for data
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = ["HLT_HIMinimumBiasHF1AND*"]

process.hltMB.andOr = cms.bool(True)  # True = OR, False = AND between the HLT paths                                                     
process.hltMB.throw = cms.bool(False) # throw exception on unknown path names

# Load you analyzer with initial configuration
process.load("Analyzers.RaghuEffTest.RaghuEffTest_cfi")

process.p = cms.Path(process.hltMB *
                     #process.eventFilter*
                     process.centralityBin *
                     process.defaultCPDC
                     )

