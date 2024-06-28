---
title: Administrative Requirements
---

# Administrative Requirements

## Introduction

Preparing to connect your system to Enterprise Event Bus may require additional interactions with VA IT teams and systems.

**Prerequisites**:

* The client has attended an Enterprise Event Bus business use case meeting.
* The client has attended an Enterprise Event Bus technical overview meeting.
* The client has received, reviewed, and signed an Enterprise Event Bus Working Agreement.

**Requirements for production**:

* The client system is registered in the VA Systems Inventory (VASI) and has a VASI ID.
* The client system has been evaluated and classified by the Enterprise Management and Support Services (eMASS) and has an eMASS ID. 
* The client system has an active Authority to Operate (ATO), or if inside the Lighthouse Delivery Infrastructure (LHDI), a continuous Authority to Operate (cATO).
* The client system has been through the System Categorization process and has a FISMA rating.
* The client system has approved PTA and PIA documents.
* Depending on the client system, an ESECC request and/or WASA scan may also be required.

## Authority to Operate (ATO)

ATO, or “Authority to Operate,” indicates that your system has been evaluated by VA and given permission to deploy code in production.

Teams that have an active ATO should review it to understand the implications of integrating with other systems.

**For Teams without an ATO**

For clients that are not LHDI tenants:

- ATO is evaluated once eMASS system registration has been completed and approved. Teams that do not have an active ATO should begin the process as early as possible in the Enterprise Event Bus integration process.

For clients that are LHDI tenants:

- Teams within the Lighthouse Delivery Infrastructure should consult their LHDI Enablement Liaison to begin the ATO process.

## Consumers of BIP-sourced Events

### OBI Access Form

Event Bus Consumers consuming a BIP-sourced event that is available on the Event Bus must follow the OBI Data Access Form process (aka the Corp DB Access Form).

If the same consumer wants to consume additional BIP-sourced events at a later time, another OBI Data Access Form must be submitted to cover the use of that additional data.

Note that if _both_ the Event Bus and the Consumer are consuming an event for the first time, the Consumer must wait for the Event Bus to submit and get approval for its own OBI Data Access Form request before submitting its own request.

[Instructions for filling out the form (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/SOP_Corporate_DB_Access_Approval%20081123%201.pdf) and [an example (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/CorpDB%20Application%20Access%20Enterprise%20Event%20Bus%20full%20production.pdf) are available in the Enterprise Event Bus GitHub repository. 

Approval must be granted first for use in non-production environments, and then for use in production. Typically access is granted for use in lower environments first. Production access is granted once proof that the team's ATO has been registered in eMASS is provided. It may be acceptable to submit only one request, as long as ATO confirmation is provided at some point during the Event Bus integration process.

### Sensitivity Filtering

The implementation of Sensitivity Filtering is required when event data, or data spawned from a callback initiated by the data, will be displayed through a VA application user interface to a VA employee or contractor.

[What is sensitivity filtering? (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/Benefits%20Information%20Sensitivity%20Filtering.md) and [instructions for implementing Sensitivity Filtering (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/Benefits%20Information%20Sensitivity%20Level%20Filtering%20Options.md) can be found in the Enterprise Event Bus GitHub repository. 

## ESECC

A request to the Enterprise Security External Change Council (ESECC) may be needed to authorize an opening in the firewall to enable a connection between the client system and the Enterprise Event Bus.

Prior to determining if your system will require an ESECC, we will attempt connecting to the Enterprise Event Bus from your system. If an error message indicates that traffic is blocked at the network level, then an ESECC is required.

If an ESECC is required, the Enterprise Event Bus team will take point on getting the request submitted. We will need the following information:

* The IP address of your system. This can be a list of specific IP addresses, a CIDR block, or a list of CIDR blocks.
* Your system's connection ID assigned by VA NSOC (Network Security Operations Center) 

## FISMA System Categorization

As part of the eMASS process, System Categorization will evaluate the impact to the organization of loss or compromise to the data in the application. The outcome of the System Categorization process is a FISMA risk level rating of Low, Moderate, or High.

If a prospective client system has not been through System Categorization, it will need to follow the steps outlined on this [GRC System Categorization page (must be on VA network to view)](https://confluence.devops.va.gov/display/VAExternal/GRC+-+System+Categorization). Note that completing a Privacy Threshold Analysis (PTA) document is a prerequisite for System Categorization.

**Note**: For teams handling ePHI (medical information specific to an individually identifiable patient), the HIPAA Security Rule applies and further review will be required. Support for this can be requested by sending an email to `VHAHCSDevelopmentSecurity2[at]va.gov`.

## PTA and PIA

A PTA, or Privacy Threshold Analysis, is a required document used to determine if a system is privacy-sensitive and requires additional privacy compliance documentation such as a PIA or SORN.  It is also the first step of the privacy compliance documentation process. 

A PIA, or Privacy Impact Assessment, is a public document that describes:  

* What PII the system is collecting  
* Why the PII is being collected
* How the PII will be collected, used, accessed, shared, safeguarded, and stored 

Whenever there is a change to the data being shared between VA systems, such as a new Event Bus integration or change to an existing Event Bus integration, the Privacy Office should be consulted, regardless of whether it is a major change or not, in order to make a determination that an updated PTA or PIA may be required.

PTAs are renewed annually and PIAs are renewed every three years, unless there are major changes. Submitting a new PTA restarts the clock on annual renewal.

*Note that all producing and consuming client systems are subject to their own PTA and PIA reviews.

Resources:

* [Privacy Threshold Analysis (PTA) and Privacy Impact Assessment (PIA) Submittal Checklist and Process Overview (PDF file, must be on VA network to view)](https://dvagov.sharepoint.com/sites/OITPrivacyHub/PTA%20Training%20Resources/Forms/AllItems.aspx?id=%2Fsites%2FOITPrivacyHub%2FPTA%20Training%20Resources%2FPTA%20and%20PIA%20Submittal%20Checklist%20and%20Process%20Overview%2Epdf&parent=%2Fsites%2FOITPrivacyHub%2FPTA%20Training%20Resources&isSPOFile=1&OR=Teams%2DHL&CT=1709826099209&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yNDAxMDQxNzUwNCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D)
* [PTA Training Resources (VA SharePoint, must be on VA network to view)]([https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/Privacy-Threshold-Analysis.aspx?csf=1&web=1&e=MY0flg](https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/PTA-Training-Resources.aspx))
* [PIA Training Resources (VA SharePoint, must be on VA network to view)]([https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/Privacy-Impact-Assessment.aspx?csf=1&web=1&e=u8YJ0w](https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/PIA-Training-Resources.aspx))

## VASI and eMASS 

The client system should either have or be in the process of procuring: 

* a VASI ID, which identifies your system in VA, and
* an eMASS ID

**Note**: The VASI and eMASS Processes have merged and are now accomplished via a single LEAF intake (formerly GRC intake) request: [Unified System Registry Intake (must be on VA network to view)](https://leaf.va.gov/NATIONAL/103/cybersecurity_request_portal/).

### VASI

The VA Systems Inventory (VASI) is intended to be a registry of all applications in use at VA. 

The Enterprise Event Bus VASI ID is 3325, and [this is our entry (must be on VA network to view)](https://vaww.vear.ea.oit.va.gov/system_and_application_domain_defs_system_381405.htm) in the VASI registry. You may find your system’s VASI ID by visiting the [VA System Inventory (must be on VA network to view)](https://vaww.vear.ea.oit.va.gov/).

**For Teams without a VASI ID**

For clients that are not LHDI tenants:

- Prospective client systems that do not have a VASI ID will need to submit a LEAF intake request to get one. 

For clients that are LHDI tenants:

- Teams on the Lighthouse Delivery Infrastructure (LHDI) should consult their LHDI Enablement Liaison to submit a LEAF intake request. 

### eMASS

Enterprise Mission Assurance Support Service (eMASS) is VA’s Governance, Risk and Compliance (GRC) tool. All systems will be assessed in eMASS by the Risk Review team for an authorization recommendation to be submitted to the Authorizing Official (AO) for final ATO consideration.

All VA systems are given an entry with a unique number in the eMASS system. The Enterprise Event Bus eMASS ID is 2350. 

Getting an eMASS ID is a prerequisite for System Categorization.

**For Teams without an eMASS ID**

For clients that are not LHDI tenants:

- Prospective client systems that do not have an eMASS ID will need to submit a LEAF intake request to get one.

For clients that are LHDI tenants:

- Teams on the Lighthouse Delivery Infrastructure (LHDI) should consult their LHDI Enablement Liaison to submit a LEAF intake request. 

## WASA Testing

Web Application Security Assessment (WASA) scanning may be needed as part of the ATO process when a client system builds a web application for consuming events from the Event Bus. Please note that a 30 day notice is required for WASA testing.

The VA SAVD WASA Coordination team can be contacted via email at `VASAVDWASACoordination[at]va.gov`. A request for WASA testing can be submitted on the [Security Assessment Portal home page (must be on VA network to view)](https://saportal.va.gov/Home).

## Other Resources

For clients that are not LHDI tenants:

- OIS Official Documentation on the VASI/eMASS/ATO process: [eMass Authorization Requirements SOP Guide (PDF file, must be on VA network to view)](https://dvagov.sharepoint.com/sites/OITOIS/KnowledgeService/eMassDocumentLibrary/eMASS_Authorization_Requirements_SOP_Guide.pdf)

For clients that are LHDI tenants:

- [Lighthouse Delivery Infrastructure Onboarding Process Overview (Mural document, view only)](https://app.mural.co/t/departmentofveteransaffairs9999/m/departmentofveteransaffairs9999/1684963245734/426a066d466aad4b985d0c6fdc1887ef18cd6a8d?invited=true&sender=u7b7ab34685f00706a24a6128)
