---
title: Administrative Requirements
---

# Administrative Requirements

## Introduction

Preparing to connect your system to Enterprise Event Bus may require additional interactions with VA IT teams, tools and systems.

**Prerequisites**:

* The client has attended an Enterprise Event Bus business use case meeting.
* The client has attended an Enterprise Event Bus technical overview meeting.
* The client has received, reviewed and signed an Enterprise Event Bus Working Agreement.

**Requirements for production**:

* The client system is registered in the VA Systems Inventory (VASI) and has a VASI ID.
* The client system has been evaluated and classified by the Enterprise Management and Support Services (eMASS) and has an eMASS ID. 
* The client system has an active Authority to Operate (ATO), or if inside the Lighthouse Delivery Infrastructure (LHDI), a continuous Authority to Operate (cATO).
* The client system has been through the System Categorization process and has a FISMA rating.
* The client system has approved PTA and PIA documents.

## VASI and eMASS 

The client system should either have or be in the process of procuring: 

* a VASI ID, which identifies your system in VA, and
* an eMASS ID

**Note**: The VASI and eMASS Processes have merged and are now accomplished via a single LEAF intake request: [Unified System Registry Intake (Formerly GRC Intake) page](https://leaf.va.gov/NATIONAL/103/cybersecurity_request_portal/) (must be on VA network to view)

### VASI

The VA Systems Inventory (VASI) is intended to be a registry of all applications in use at VA. 

The Enterprise Event Bus VASI ID is 3325, and [this is our entry](https://vaww.vear.ea.oit.va.gov/system_and_application_domain_defs_system_381405.htm) in the VASI registry. You may find your system’s VASI ID by visiting the [VA System Inventory](https://vaww.vear.ea.oit.va.gov/). (must be on VA network to view)

**For non-LHDI clients**:

* If a prospective client system does not have a VASI ID, it will need to submit a LEAF intake request to get one. 

**For new LHDI clients**:

* For new teams on Lighthouse Delivery Infrastructure (LHDI), please consult your LHDI Enablement Liaison to start the LEAF intake request and LHDI-specific onboarding. 

### eMASS

Enterprise Mission Assurance Support Service (eMASS), VA’s Governance, Risk and Compliance (GRC) tool, is the authoritative management tool for VA’s Assessment and Authorization (A&A) process and Risk Management Framework. All systems will be assessed in eMASS by the Risk Review team for an authorization recommendation to be submitted to the Authorizing Official (AO) for final ATO consideration.

All VA systems are given an entry with a unique number in the eMASS system. The Enterprise Event Bus eMASS ID is 2350. 

Getting an eMASS ID is a prerequisite for [System Categorization](#fisma-system-categorization). 

**For non-LHDI clients**:

* If a prospective client system does not have an eMASS ID, it will need to submit a [LEAF intake request](https://leaf.va.gov/NATIONAL/103/cybersecurity_request_portal/) to get one.

**For new LHDI clients**:

* For new teams on Lighthouse Delivery Infrastructure (LHDI), please consult your LHDI Enablement Liaison to start the LEAF intake request process and LHDI-specific onboarding. 

## Authority to Operate (ATO)

ATO, or “Authority to Operate,” indicates that your system has been evaluated by VA and given permission to deploy code in production.

Client teams that have an active ATO should review it to understand the implications of integrating with the Enterprise Event Bus. That information should be shared with the Enterprise Event Bus team so that both parties understand each other’s requirements for deploying code to production.

**For non-LHDI clients**:

ATO is evaluated once eMASS system registration has been completed and approved. Teams that do not have an active ATO should begin the process as early as possible in the Enterprise Event Bus integration process.

**For new LHDI clients**:

For new teams within the Lighthouse Delivery Infrastructure, please consult your LHDI Enablement Liaison to begin the ATO process.

## FISMA - System Categorization

As part of the eMASS process, System Categorization will evaluate the impact to the organization of loss or compromise to the data in the application. The outcome of the System Categorization process is a FISMA risk level rating of Low, Moderate, or High.

If a prospective client system has not been through System Categorization, it will need to follow the steps outlined on this [(LHDI) GRC System Categorization page](https://confluence.devops.va.gov/display/VAExternal/GRC+-+System+Categorization). Note that completing a Privacy Threshold Analysis (PTA) document is a prerequisite for System Categorization.

**Note**: For teams handling ePHI (medical information specific to an individually identifiable patient), the HIPAA Security Rule applies and further review will be required. Support for this can be requested by sending an email to [VHAHCSDevelopmentSecurity2@va.gov](mailto:VHAHCSDevelopmentSecurity2@va.gov).

## PTA and PIA

Privacy Threshold Analysis (PTA) and Privacy Impact Assessment (PIA) documents address what data is crossing what boundaries - this changes for both the Enterprise Event Bus and the client system when a new (producing or consuming) system is added to the bus. When this happens, Enterprise Event Bus becomes a system that clients share data with, so PTA/PIA updates are likely in order for both the Enterprise Event Bus and the new client system.

PTAs are renewed annually and PIAs are renewed every 3 years, unless there are major changes. Submitting a new PTA restarts the clock on annual renewal.

In summary, every time there is a change to working VA data, the Privacy Office needs to be engaged, regardless of whether it is a major change or not, in order to make a determination. If there is concurrence from the ISO and ISSO that a new PTA should be submitted, PIA Support will decide if the PIA needs to be renewed when evaluating the submitted PTA.

*Note that producing and consuming systems are subject to their own PTA and PIA reviews to ensure best practices are followed.

Resources:

* [Privacy Threshold Analysis (PTA) and Privacy Impact Assessment (PIA) Submittal Checklist and Process Overview](https://dvagov.sharepoint.com/sites/OITPrivacyHub/PTA%20Training%20Resources/Forms/AllItems.aspx?id=%2Fsites%2FOITPrivacyHub%2FPTA%20Training%20Resources%2FPTA%20and%20PIA%20Submittal%20Checklist%20and%20Process%20Overview%2Epdf&parent=%2Fsites%2FOITPrivacyHub%2FPTA%20Training%20Resources&isSPOFile=1&OR=Teams%2DHL&CT=1709826099209&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yNDAxMDQxNzUwNCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D) (pdf, must be on VA network to view)
* [PTA Training Resources](https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/Privacy-Impact-Assessment.aspx?csf=1&web=1&e=u8YJ0w) (VA SharePoint, must be on VA network to view)

## ESECC

Depending on the operating boundaries or ports used by the client system, a request to the Enterprise Security External Change Council (ESECC) may be needed to authorize an opening in the firewall to enable a connection between the client system and the Enterprise Event Bus.

Prior to determining if your system will require an ESECC, teams are highly encouraged to first attempt connecting to the Enterprise Event Bus.

![A diagram showing various possibilities and whether a system would likely need an ESECC. If you are on Amazon Web Services (AWS) inside VA Enterprise Cloud (VAEC), or on LHDI, no ESECC is needed. Instead, a Service Now ticket is needed. If you are on AWS outside VAE, or if you are on Non-AWS Cloud (e.g. Azure), you should check if ESECC is needed. If you are on Premise, e.g., VistA, an ESECC is needed.](img/Client-Environments-ESECC-Decision-Circles.svg)

Resources:

* [ESECC Public URL process (GitHub)](https://github.com/department-of-veterans-affairs/devops/blob/master/docs/ESECC-Public-URL-process.md#prereq)
* [Tutorial video](https://dvagov.sharepoint.com/:v:/r/sites/OITECOESDKM/KM%20video%20library/Stream%20Migrated%20Videos/Knowledge%20Management%20Videos/KB0106755%20-%20Network%20ESECC%20-%20Create%20a%20Change%20Request-20221206_034448.mp4?csf=1&web=1&e=cCAS5z&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D) on creating a Change Request in ESECC
* [ESECC Self-service Portal](https://esecc.va.gov/CGWeb/Main.aspx) for initiating new requests or change requests

## WASA Testing

Web Application Security Assessment (WASA) scanning may be needed when a client system builds a web application for consuming events from the bus.

The VA SAVD WASA Coordination team can be contacted via email at [VASAVDWASACoordination@va.gov](mailto:VASAVDWASACoordination@va.gov). A request for WASA testing can be submitted on the [Security Assessment Portal home page](https://portalapps.vansoc.va.gov/EAS/Home).

## Other Resources

**For non-LHDI clients**:

OIS Official Documentation on the VASI/eMASS/ATO process: [eMass Authorization Requirements SOP Guide](https://dvagov.sharepoint.com/sites/OITOIS/KnowledgeService/eMassDocumentLibrary/eMASS_Authorization_Requirements_SOP_Guide.pdf) (pdf)

**For new LHDI clients**:

[Lighthouse Delivery Infrastructure Onboarding Process Overview](https://app.mural.co/t/departmentofveteransaffairs9999/m/departmentofveteransaffairs9999/1684963245734/426a066d466aad4b985d0c6fdc1887ef18cd6a8d?invited=true&sender=u7b7ab34685f00706a24a6128) (Mural)