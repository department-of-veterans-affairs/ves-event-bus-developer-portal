---
title: Start Guide and Administrative Requirements
---

# **Start Guide and Administrative Requirements** 
## **Start Guide**

This guide covers everything you need to integrate with the Enterprise Event Bus from planning your approach to completing technical set up. Working through these steps can seem daunting, but the Event Bus team is here to support you through this process. 

**Product Planning**

Before diving into technical details, take some time to clarify your goals and approach: 
- What problem are you solving? Document current pain points, inefficiencies, or limitations that event-driven architecture would address
- What is the desired outcome? Define specific improvements you expect to achieve
- How might you define and track success metrics? Identify measurable indicators like reduced latency, improved consistency, or enhanced user experience
- What is the timeline for this work? Consider the priority level and whether external deadlines, dependencies, or key milestones will influence when this needs to be completed.
- Have you identified data sources? While not required upfront, knowing which systems generate the events you need and who owns that data will streamline discussions and technical planning.

**Getting Connected**

Once you’ve thought through your use case, here’s how to get the ball rolling:

- Set a meeting with Enterprise Event Bus to discuss use case and technical overview
  - You can find information on reaching out on the Contact and Support Page
- Collaborate on a Working Agreement- the Enterprise Event Bus will draft this based on your discussion 
- Review and sign Enterprise Event Bus Working Agreement

**System Registration**

You’ll need to gather system identification information. This helps the Event Bus team verify the system is authorized to connect and handle data appropriately:  

- Identify your VA Systems Inventory (VASI) ID
- Identify your Enterprise Mission Assurance Support Service (eMASS) ID
  - As part of setting up your eMASS ID you should have already completed the System Categorization process to obtain a FISMA rating (Low, Moderate, or High)
- Identify your Authority to Operate (ATO) (or cATO if in LHDI)
- If building a web application, request Web Application Security Assessment (WASA) (requires 30-day notice)

Note: If you do not already have an eMASS ID, VASI ID, and an ATO/cATO you will need to submit a LEAF intake request for the ones you are missing (LHDI tenants will need to consult with their LHDI Enablement Liaison)

**Privacy Documentation**

These documents help ensure data protection compliance: 

- Complete Privacy Threshold Analysis (PTA)
- Complete Privacy Impact Assessment (PIA)

**Special Requirements**

Depending on your specific use case, you may also need to complete:

- OBI Data Access Form, which is required for BIP-sourced events 
- Sensitivity Filtering implementation,  which is required for VA application user interfaces accessing the Corporate database

**Network Configuration**

Finally, let’s make sure your systems can talk with Event Bus:

- Test connection from your system to Enterprise Event Bus
  - If you are blocked, work with the Event Bus team to submit an Enterprise Security External Change Council (ESECC) request
    - You will need to provide IP addresses (or CIDR blocks) and your system's connection ID assigned by VA NSOC


**You can find more details on each of these topics below**

## **Authority to Operate (ATO)**

ATO, or “Authority to Operate,” indicates that your system has been evaluated by VA and given permission to deploy code in production.

Teams that have an active ATO should review it to understand the implications of integrating with other systems.

**For Teams without an ATO**

For clients that are not LHDI tenants:

- ATO is evaluated once eMASS system registration has been completed and approved. Teams that do not have an active ATO should begin the process as early as possible in the Enterprise Event Bus integration process.

For clients that are LHDI tenants:

- Teams within the Lighthouse Delivery Infrastructure should consult their LHDI Enablement Liaison to begin the ATO process.

## **WASA Testing**

Web Application Security Assessment (WASA) scanning may be needed as part of the ATO process when a client system builds a web application for consuming events from the Event Bus. Please note that a 30 day notice is required for WASA testing.

The VA SAVD WASA Coordination team can be contacted via email at `VASAVDWASACoordination[at]va.gov`. A request for WASA testing can be submitted on the [Security Assessment Portal home page (must be on VA network to view)](https://saportal.va.gov/Home).

## **VASI and eMASS** 

The client system should either have or be in the process of procuring: 

* a VASI ID, which identifies your system in VA, and
* an eMASS ID

**Note**: The VASI and eMASS Processes have merged and are now accomplished via a single LEAF intake (formerly GRC intake) request: [Unified System Registry Intake (must be on VA network to view)](https://leaf.va.gov/NATIONAL/103/cybersecurity_request_portal/).

### **VASI**

The VA Systems Inventory (VASI) is intended to be a registry of all applications in use at VA. 

The Enterprise Event Bus VASI ID is 3325, and [this is our entry (must be on VA network to view)](https://vaww.vear.ea.oit.va.gov/system_and_application_domain_defs_system_381405.htm) in the VASI registry. You may find your system’s VASI ID by visiting the [VA System Inventory (must be on VA network to view)](https://vaww.vear.ea.oit.va.gov/).

**For Teams without a VASI ID**

For clients that are not LHDI tenants:

- Prospective client systems that do not have a VASI ID will need to submit a LEAF intake request to get one. 

For clients that are LHDI tenants:

- Teams on the Lighthouse Delivery Infrastructure (LHDI) should consult their LHDI Enablement Liaison to submit a LEAF intake request. 

### **eMASS**

Enterprise Mission Assurance Support Service (eMASS) is VA’s Governance, Risk and Compliance (GRC) tool. All systems will be assessed in eMASS by the Risk Review team for an authorization recommendation to be submitted to the Authorizing Official (AO) for final ATO consideration.

All VA systems are given an entry with a unique number in the eMASS system. The Enterprise Event Bus eMASS ID is 2350. 

Getting an eMASS ID is a prerequisite for System Categorization.

**For Teams without an eMASS ID**

For clients that are not LHDI tenants:

- Prospective client systems that do not have an eMASS ID will need to submit a LEAF intake request to get one.

For clients that are LHDI tenants:

- Teams on the Lighthouse Delivery Infrastructure (LHDI) should consult their LHDI Enablement Liaison to submit a LEAF intake request. 


## **FISMA System Categorization**

As part of the eMASS process, System Categorization will evaluate the impact to the organization of loss or compromise to the data in the application. The outcome of the System Categorization process is a FISMA risk level rating of Low, Moderate, or High.

If a prospective client system has not been through System Categorization, it will need to follow the steps outlined on this [GRC System Categorization page (must be on VA network to view)](https://confluence.devops.va.gov/display/VAExternal/GRC+-+System+Categorization). Note that completing a Privacy Threshold Analysis (PTA) document is a prerequisite for System Categorization.

**Note**: For teams handling ePHI (medical information specific to an individually identifiable patient), the HIPAA Security Rule applies and further review will be required. Support for this can be requested by sending an email to `VHAHCSDevelopmentSecurity2[at]va.gov`.


## **Consumers of BIP-sourced Events**

### **OBI Access Form**

Event Bus Consumers consuming a BIP-sourced event that is available on the Event Bus must follow the OBI Data Access Form process (aka the Corp DB Application Access Form).

**Who needs to submit an approval request?**

Anyone who needs to access Corporate database data and has not been previously approved for that specific purpose must submit a request.

Examples:

* Any entity (Event Bus or an Event Bus Consumer) accessing Corporate data for the first time. 
* Any entity (Event Bus or an Event Bus Consumer) who currently accesses specific Corporate data through an event on the Event Bus but now needs access to different data.
* Any entity who wants to use the Corporate data they have access to for a different purpose than what was previously approved; for example, An Event Bus Consumer has been using an event sourced from Corp DB data to trigger notifications and now wants to use that same event to automatically update data in another VA system.
* Any entity accessing Corporate data through a third party; for example, when a system consumes a BIP-sourced event from the Event Bus.

**Note:** If _both_ the Event Bus and the Consumer are consuming an event for the first time, the Consumer must wait for the Event Bus to submit and get approval for its own OBI Data Access Form request before submitting its own request.

[Instructions for filling out the OBI Data Access form (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/SOP_Corporate_DB_Access_Approval%20081123%201.pdf) and [an example of the OBI Data Access form (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/CorpDB%20Application%20Access%20Enterprise%20Event%20Bus%20full%20production.pdf) are available in the Enterprise Event Bus GitHub repository. 

While permission may be granted to access Corp DB data for use in both non-production and production environments, there are cases, such as when a team is in the process of obtaining its ATO, that access may be granted for use in lower environments first, with production access granted once the team's ATO has been registered in eMASS. In the case of the latter, it may be acceptable to submit only one request, as long as ATO confirmation is provided at some point during the Event Bus integration process.

### **Sensitivity Filtering**

The implementation of Sensitivity Filtering is required when event data, or data spawned from a callback initiated by the data, will be displayed through a VA application user interface to a VA employee or contractor.

[An article on sensitivity filtering (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/Benefits%20Information%20Sensitivity%20Filtering.md) and [instructions for implementing Sensitivity Filtering (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Partner%20Teams/BIP%20Meetings%20and%20Materials/Benefits%20Information%20Sensitivity%20Level%20Filtering%20Options.md) can be found in the Enterprise Event Bus GitHub repository. 

## **ESECC**

A request to the Enterprise Security External Change Council (ESECC) may be needed to authorize an opening in the firewall to enable a connection between the client system and the Enterprise Event Bus.

Prior to determining if your system will require an ESECC, we will collaborate on testing a connection from your system to the Enterprise Event Bus. If an error message indicates that traffic is blocked at the network level, then an ESECC will be required.

If an ESECC is required, the Enterprise Event Bus team will submit the ESECC request on your team's behalf. We will need the following information:

* The IP address of your system. This can be a list of specific IP addresses or CIDR blocks. If your system is deployed to a few IP addresses that are always the same, then we will use those specific IP addresses. If your system is deployed to different IP addresses within a CIDR block or a few CIDR blocks, then we'll use CIDR blocks.
* Your system's connection ID assigned by VA NSOC (VA Network Security Operations Center).


## **PTA and PIA**

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
* [PTA Training Resources (VA SharePoint, must be on VA network to view)](https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/PTA-Training-Resources.aspx)
* [PIA Training Resources (VA SharePoint, must be on VA network to view)](https://dvagov.sharepoint.com/sites/OITPrivacyHub/SitePages/PIA-Training-Resources.aspx)


## **Other Resources**

For clients that are not LHDI tenants:

- OIS Official Documentation on the VASI/eMASS/ATO process: [eMass Authorization Requirements SOP Guide (PDF file, must be on VA network to view)](https://dvagov.sharepoint.com/sites/OITOIS/KnowledgeService/eMassDocumentLibrary/eMASS_Authorization_Requirements_SOP_Guide.pdf)

For clients that are LHDI tenants:

- [Lighthouse Delivery Infrastructure Onboarding Process Overview (Mural document, view only)](https://app.mural.co/t/departmentofveteransaffairs9999/m/departmentofveteransaffairs9999/1684963245734/426a066d466aad4b985d0c6fdc1887ef18cd6a8d?invited=true&sender=u7b7ab34685f00706a24a6128)
