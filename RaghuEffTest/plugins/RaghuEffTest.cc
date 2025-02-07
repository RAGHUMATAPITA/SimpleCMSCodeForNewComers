// -*- C++ -*-
//   
//         Author: Raghunath Pradhan
//         Class: RaghuEffTest 
//         Date created on April 8, 2024
//         miniAOD / AOD
//         

// CMSSW include files
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

// user include files
#include "Analyzers/RaghuEffTest/interface/RaghuEffTest.h"
#include <string>

//  constructors and destructor

RaghuEffTest::RaghuEffTest(const edm::ParameterSet& iConfig) :  //Parametrized Constructor
  //******TRACKED PARAMETER********
  
  //tracks & vertex
  //trackTags_(consumes< edm::View< pat::PackedCandidate> >(iConfig.getParameter<edm::InputTag>("tracks"))), // uncomment for MAOD
  //trackTagsgen_(consumes< edm::View< pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("tracksgen"))), // uncomment for MAOD
  
  trackTags_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("tracks"))), // uncomment for AOD
  trackTagsgen_(consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("tracksgen"))), // uncomment for AOD
  
  //chi2Map_( consumes< edm::ValueMap< float > >( iConfig.getParameter< edm::InputTag >( "trackschi2" ) ) ), // uncomment for MAOD
  vtxTags_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertex"))),

  //centrality bin
  cent_bin_(consumes<int>(iConfig.getParameter<edm::InputTag>("centralitybin"))),
  
  //******UNTRACKED PARAMETER****************
  //vertex selection
  zminVtx_(iConfig.getUntrackedParameter<double>("zminVtx")),
  zmaxVtx_(iConfig.getUntrackedParameter<double>("zmaxVtx")),

  //EFF Correction
  fGeneral_(iConfig.getUntrackedParameter<edm::InputTag>("fGeneral")),
  fGeneral2_(iConfig.getUntrackedParameter<edm::InputTag>("fGeneral2")),

  //binning
  pTBins_(iConfig.getUntrackedParameter< std::vector < double > >("pTBins")),
  etaBins_(iConfig.getUntrackedParameter< std::vector < double > >("etaBins")),
  centbins_(iConfig.getUntrackedParameter< std::vector < double > >("centbins")),
  algoParameters_(iConfig.getParameter< std::vector < int > >("algoParameters"))
{  
  //*****Defining Histograms & Profile Histograms********************                  
  TH1::SetDefaultSumw2();
  TH2::SetDefaultSumw2();
  TH3::SetDefaultSumw2();

  //**************************For efficiency correction ******************************************************
  feff_ = 0x0; 
  TString f_General(fGeneral_.label().c_str());
  if(!f_General.IsNull())
    {
      edm::FileInPath f1 (Form("Analyzers/RaghuEffTest/data/EFF/general_tracks/%s",f_General.Data()));
      feff_ = new TFile(f1.fullPath().c_str(),"READ");
      //trkEff = new TrkEff2018PbPb("general", "", false, "/afs/cern.ch/work/r/rpradhan/Tracking_Studies/newCode_AfterRun3/ForEffTest/CMSSW_13_2_5_patch1/src/Analyzers/RaghuEffTest/data/EFF/general_tracks");
      
      std::cout<<"efficiecny file name is: "<<feff_->GetName()<<std::endl;
    }

  feff2_ = 0x0; 
  TString f_General2(fGeneral2_.label().c_str());
  if(!f_General2.IsNull())
    {
      edm::FileInPath f2 (Form("Analyzers/RaghuEffTest/data/EFF/general_tracks/%s",f_General2.Data()));
      feff2_ = new TFile(f2.fullPath().c_str(),"READ");
      //trkEff = new TrkEff2018PbPb("general", "", false, "/afs/cern.ch/work/r/rpradhan/Tracking_Studies/newCode_AfterRun3/ForEffTest/CMSSW_13_2_5_patch1/src/Analyzers/RaghuEffTest/data/EFF/general_tracks");
      
      std::cout<<"efficiecny2 file name is: "<<feff2_->GetName()<<std::endl;
    }

  hEff3D = (TH3F*)feff2_->Get("hEff_3D");
  hFak3D = (TH3F*)feff_->Get("hFak_3D");
  hSec3D = (TH3F*)feff_->Get("hSec_3D");
  hMul3D = (TH3F*)feff_->Get("hMul_3D");
  
  feff_->Close();
  feff2_->Close();

  usesResource("TFileService");
  edm::Service<TFileService> fs;

  TFileDirectory fGlobalHist = fs->mkdir("QAplots");
  hZBestVtx    = fGlobalHist.make<TH1F>("hZvtx", "", 600, -30.0, 30.0);
  hcent_bin    = fGlobalHist.make<TH1F>("hcent_bin", "", 200, 0.0, 200.0);
  hcentbin     = fGlobalHist.make<TH1F>("hcentbin", "", centbins_.size()-1, &centbins_[0]);
  
  //*************************************************
  //hptbin     = fGlobalHist.make<TH1F>("hptbin", "", 30, 0., 3.);
  hptbin     = fGlobalHist.make<TH1F>("hptbin", "", 500, 0., 50.);
  hetabin     = fGlobalHist.make<TH1F>("hetabin", "", etaBins_.size()-1, &etaBins_[0]);
  
  // gen
  hpt_gen.resize(centbins_.size());
  heta_gen.resize(centbins_.size());
  hphi_gen.resize(centbins_.size());

  // reco
  hpt.resize(centbins_.size());
  heta.resize(centbins_.size());
  hphi.resize(centbins_.size());
  hnHits.resize(centbins_.size());
  hptreso.resize(centbins_.size());
  hchi2.resize(centbins_.size());
  hDCAZ.resize(centbins_.size());
  hDCAXY.resize(centbins_.size());

  // reco corrected
  hpt_eff.resize(centbins_.size());
  heta_eff.resize(centbins_.size());
  hphi_eff.resize(centbins_.size());
  hnHits_eff.resize(centbins_.size());
  hptreso_eff.resize(centbins_.size());
  hchi2_eff.resize(centbins_.size());
  hDCAZ_eff.resize(centbins_.size());
  hDCAXY_eff.resize(centbins_.size());

  for(unsigned int i = 0; i < centbins_.size(); i++)
    {
      //gen
      //hpt_gen[i]          = fGlobalHist.make<TH1F>(Form("hpt_gen_%d", i), "", 30, 0., 3.);
      hpt_gen[i]          = fGlobalHist.make<TH1F>(Form("hpt_gen_%d", i), "", 500, 0., 50.);
      heta_gen[i]         = fGlobalHist.make<TH1F>(Form("heta_gen_%d",i), "", etaBins_.size()-1, &etaBins_[0]);
      hphi_gen[i]         = fGlobalHist.make<TH1F>(Form("hphi_gen_%d",i), "", 62, -TMath::Pi(), TMath::Pi());

      //reco
      //hpt[i]              = fGlobalHist.make<TH1F>(Form("hpt_%d", i), "", 30, 0., 3.);
      hpt[i]              = fGlobalHist.make<TH1F>(Form("hpt_%d", i), "", 500, 0., 50.);
      heta[i]             = fGlobalHist.make<TH1F>(Form("heta_%d", i), "", etaBins_.size()-1, &etaBins_[0]);
      hphi[i]             = fGlobalHist.make<TH1F>(Form("hphi_%d", i), "", 62, -TMath::Pi(), TMath::Pi());
      hnHits[i]           = fGlobalHist.make<TH1F>(Form("hnHits_%d", i), "", 50, 0., 50.);
      hptreso[i]          = fGlobalHist.make<TH1F>(Form("hptreso_%d", i), "", 100, 0., 1.);
      hchi2[i]            = fGlobalHist.make<TH1F>(Form("hchi2_%d", i), "", 100, 0, 10.);
      hDCAZ[i]            = fGlobalHist.make<TH1F>(Form("hDCAZ_%d", i), "", 80, -4., 4.);
      hDCAXY[i]           = fGlobalHist.make<TH1F>(Form("hDCAXY_%d", i), "", 80, -4., 4.);

      //reco corrected
      //hpt_eff[i]          = fGlobalHist.make<TH1F>(Form("hpt_eff_%d", i), "", 30, 0., 3.);
      hpt_eff[i]          = fGlobalHist.make<TH1F>(Form("hpt_eff_%d", i), "", 500, 0., 50.);
      heta_eff[i]         = fGlobalHist.make<TH1F>(Form("heta_eff_%d", i), "", etaBins_.size()-1, &etaBins_[0]);
      hphi_eff[i]         = fGlobalHist.make<TH1F>(Form("hphi_eff_%d", i), "", 62, -TMath::Pi(), TMath::Pi());
      hnHits_eff[i]       = fGlobalHist.make<TH1F>(Form("hnHits_eff_%d", i), "", 50, 0., 50.);
      hptreso_eff[i]      = fGlobalHist.make<TH1F>(Form("hptreso_eff_%d", i), "", 100, 0., 1.);
      hchi2_eff[i]        = fGlobalHist.make<TH1F>(Form("hchi2_eff_%d", i), "", 100, 0, 10.);
      hDCAZ_eff[i]        = fGlobalHist.make<TH1F>(Form("hDCAZ_eff_%d", i), "", 80, -4., 4.);
      hDCAXY_eff[i]       = fGlobalHist.make<TH1F>(Form("hDCAXY_eff_%d", i), "", 80, -4., 4.);
    }
}


RaghuEffTest::~RaghuEffTest() // Destructor 
{
}

//---------------method called for each event-------------------------------------------------------

void
RaghuEffTest::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  LoopCMWVertices(iEvent, iSetup);

}

//----------------method called once each job just before starting event loop---------------------------

void
RaghuEffTest::beginJob()
{
}

//-------------method called once each job just before ending the event loop--------------------------------------------

void
RaghuEffTest::endJob()
{
}

//==============================================================================================

void
RaghuEffTest::fillDescriptions(edm::ConfigurationDescriptions&  descriptions)
{
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//=============================================================================

void
RaghuEffTest::LoopCMWVertices( const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;

  //track collection
  auto trks = iEvent.getHandle( trackTags_ );
  auto trksgen = iEvent.getHandle( trackTagsgen_ );

  // access tracks chi2/ndf
  //auto chi2Map = iEvent.getHandle( chi2Map_ ); // uncomment for MAOD

  //vtx collection
  auto pvs = iEvent.getHandle( vtxTags_ );

  //best vertex
  double bestvzError, bestvxError, bestvyError;
  math::XYZPoint bestvtx;
  math::Error<3>::type vtx_cov;
  if ( !pvs->empty() )
    {
      const reco::Vertex& vtx = (*pvs)[0];
      bestvzError = vtx.zError();
      bestvxError = vtx.xError();
      bestvyError = vtx.yError();
      bestvtx = vtx.position();
      vtx_cov = vtx.covariance();      
    }
  else
    { 
      return; 
    }

  xBestVtx_ = bestvtx.x();
  yBestVtx_ = bestvtx.y();
  zBestVtx_ = bestvtx.z();
  
  if ( zBestVtx_ < zminVtx_ || zBestVtx_ >= zmaxVtx_ ) return; 

  // ----------------- centrality selection -------------------------------

  // access centrality bins
  auto cbin = iEvent.getHandle( cent_bin_ );
  float centralityBin = ( float ) (*cbin);

  int centbin = hcentbin->FindBin(centralityBin) -1;

  hZBestVtx -> Fill(zBestVtx_); 
  hcent_bin -> Fill(centralityBin);
  
  //********* start track loop *********
  // gen loop~~~~~~~~~~
  for (auto const& iter_tk_gn : *trksgen)
    {
      if(iter_tk_gn.status() != 1) continue;
      
      // Get eta, pt, and charge of the track
      double gen_pt = iter_tk_gn.pt();
      double gen_eta = iter_tk_gn.eta();
      int gen_charge = iter_tk_gn.charge();
      double gen_phi = iter_tk_gn.phi();
      
      //selected tracks
      if( gen_charge == 0 ) continue;
      //if( gen_pt <= 0.3 || gen_pt >= 3.0 ) continue;
      if( gen_pt <= 0.3 || gen_pt >= 50.0 ) continue;
      if( gen_eta <= -2.4 || gen_eta >= 2.4 ) continue;

      hpt_gen[centbin]->Fill(gen_pt);
      heta_gen[centbin]->Fill(gen_eta);
      hphi_gen[centbin]->Fill(gen_phi);
    }

  // reco loop~~~~~~~~~~
  int trkIndx = -1;
  // Loop over tracks

  for (auto const& iter_tk : *trks) // uncoment for AOD 
  //for (auto const& trk : *trks) // uncoment for miniAOD
    {
      trkIndx++;

      // uncomment  for MAOD
      //if ( !trk.hasTrackDetails() ) continue;
      //auto iter_tk = trk.pseudoTrack();

      double pterror = iter_tk.ptError();
      double vzErr=bestvzError;
      double vxErr=bestvxError;
      double vyErr=bestvyError;

      double dxy = iter_tk.dxy(bestvtx);
      double dz = iter_tk.dz(bestvtx);
      double dxysigma = sqrt(iter_tk.d0Error()*iter_tk.d0Error()+vxErr*vyErr);
      double dzsigma = sqrt(iter_tk.dzError()*iter_tk.dzError()+vzErr*vzErr);
      
      // Get eta, pt, and charge of the track
      double pt = iter_tk.pt();
      double eta = iter_tk.eta();
      int charge = iter_tk.charge();
      double phi = iter_tk.phi();
      auto hit_pattern = iter_tk.hitPattern();
      
      //HI specific cuts
      //double chi2ndof = ( double ) ( *chi2Map )[ trks->ptrAt( trkIndx ) ]; // uncomment for MAOD
      double chi2ndof = iter_tk.normalizedChi2(); // uncomment for AOD
      double dcaxy = (dxy/dxysigma);
      double dcaz = (dz/dzsigma);
      double ptreso = (fabs(pterror) / pt);
      int nHits = iter_tk.numberOfValidHits();
      double chi2n = ( chi2ndof / hit_pattern.trackerLayersWithMeasurement() );
      int algo  = iter_tk.algo();
      
      //selected tracks
      if( charge == 0 ) continue;
      if( iter_tk.quality(reco::TrackBase::qualityByName("highPurity")) != 1 ) continue;
      //if( ptreso > 99999999.0 ) continue; // 0.1 nominal
      //if( ptreso < 0.) continue; // original
      if(pt > 10)
	{
	  if( ptreso > 0.1) continue;
	}
      else
	{
	  if( ptreso < 0.) continue;
	}
      
      if( fabs(dcaz) > 3.0 ) continue;
      if( fabs(dcaxy) > 3.0 ) continue;
      //if( chi2n > 99999999.0) continue; //0.18
      if( chi2n < 0.) continue;
      if( nHits < 0. ) continue;
      
      int count = 0;
      for(unsigned i = 0; i < algoParameters_.size(); i++)
	{
	  if( algo == algoParameters_[i] ) count++;
	}
      if( count == 0 ) continue;
      
      
      //if( pt <= 0.3 || pt >= 3.0 ) continue;
      if( pt <= 0.3 || pt >= 50.0 ) continue;
      if( eta <= -2.4 || eta >= 2.4 ) continue;
      
      float eff = hEff3D->GetBinContent(hEff3D->GetXaxis()->FindBin(eta), hEff3D->GetYaxis()->FindBin(pt), hEff3D->GetZaxis()->FindBin(centralityBin));
      float fak = hFak3D->GetBinContent(hFak3D->GetXaxis()->FindBin(eta), hFak3D->GetYaxis()->FindBin(pt), hFak3D->GetZaxis()->FindBin(centralityBin));
      float sec = hSec3D->GetBinContent(hSec3D->GetXaxis()->FindBin(eta), hSec3D->GetYaxis()->FindBin(pt), hSec3D->GetZaxis()->FindBin(centralityBin));
      float mul = hMul3D->GetBinContent(hMul3D->GetXaxis()->FindBin(eta), hMul3D->GetYaxis()->FindBin(pt), hMul3D->GetZaxis()->FindBin(centralityBin));

      float weight = (1. - fak)/eff;

      //float correction = trkEff->getCorrection(pt, eta, (int)centralityBin);

      //std::cout<<"Correction factor is: "<<weight<<"  "<<correction<<std::endl;
      
      //float weight = ((1.0 - fak)*(1.0 - sec))/(eff*(1.0 + mul));
      
      //=========Filling histograms======================
      hpt[centbin]->Fill(pt);
      heta[centbin]->Fill(eta);
      hphi[centbin]->Fill(phi);
      hnHits[centbin]->Fill(nHits);
      hptreso[centbin]->Fill(ptreso);
      hchi2[centbin]->Fill(chi2n);
      hDCAZ[centbin]->Fill(dcaz);
      hDCAXY[centbin]->Fill(dcaxy);
      
      hpt_eff[centbin]->Fill(pt, weight);
      heta_eff[centbin]->Fill(eta, weight);
      hphi_eff[centbin]->Fill(phi, weight);
      hnHits_eff[centbin]->Fill(nHits, weight);
      hptreso_eff[centbin]->Fill(ptreso, weight);
      hchi2_eff[centbin]->Fill(chi2n, weight);
      hDCAZ_eff[centbin]->Fill(dcaz, weight);
      hDCAXY_eff[centbin]->Fill(dcaxy, weight);
    } //end of Track loop
  

}//end of LoopCMWVertices

DEFINE_FWK_MODULE(RaghuEffTest);
