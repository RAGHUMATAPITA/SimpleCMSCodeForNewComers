import FWCore.ParameterSet.Config as cms

defaultCPDC = cms.EDAnalyzer('RaghuEffTest', #Analyzer named: Correspond to the class name in 'plugin' folder
                             #tracks = cms.InputTag("packedPFCandidates"), # for MAOD
                             #tracksgen = cms.InputTag("packedGenParticles"), # for MAOD
                             #trackschi2 = cms.InputTag("packedPFCandidateTrackChi2"), # for MAOD
                             #vertex = cms.InputTag("offlineSlimmedPrimaryVertices"), # for MAOD
                             
                             tracks = cms.InputTag("generalTracks"),
                             tracksgen = cms.InputTag("genParticles"),
                             vertex = cms.InputTag("offlinePrimaryVertices"),
                             
                             centralitybin = cms.InputTag("centralityBin", "HFtowers"),
                             
                             # Vertex selection
                             zminVtx = cms.untracked.double(-15.0),  ## Default = -15.0
                             zmaxVtx = cms.untracked.double(15.0),   ## Default = 15.0
                             
                             # Efficiency 
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0.root"),
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_V0.root"),
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_nopTResChi2_V0.root"),
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_noChi2Cut_ptGt10ptResoCut_Nominal_V0.root"),
                             fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_noChi2Cut_ptGt10ptResoCut_Nominal_NewSample.root"),
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_V1.root"),
                             #fGeneral = cms.untracked.InputTag("General_TrackEff_3D_nhits0_V2.root"),
                             fGeneral2 = cms.untracked.InputTag("General_TrackEff_3D_nhits0_noChi2Cut_ptGt10ptResoCut_Nominal_NewSampleQCD.root"),
                             pTBins = cms.untracked.vdouble(0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7,
                                                  0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7,
                                                  1.8, 1.9, 2.0, 2.5, 3.0),
                             etaBins = cms.untracked.vdouble(-3.0, -2.4, -2.0, -1.6, -1.2, -0.8, -0.4, 0.0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 3.0),
                             #etaBins = cms.untracked.vdouble(-3.0, -2.4, -2.0, -1.6, -1.4, -1.3, -1.2, -1.0, -0.8, -0.4, 0.0, 0.4, 0.8, 1.0, 1.2, 1.3, 1.4, 1.6, 2.0, 2.4, 3.0),
                             centbins = cms.untracked.vdouble(0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0),
                             #centbins = cms.untracked.vdouble(0.0, 10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0),
                             algoParameters = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46)
)
