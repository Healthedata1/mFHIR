[<<back](../README.md)
<!---
tags: omh2fhir
title: wide-template
--->

<!-- icons -->
<header>
<a href="https://www.openmhealth.org/">
<img style="float: left" width="25%" height="25%" src="https://www.openmhealth.org/wp-content/themes/openmhealth2015/dist/images/logo@2x.png" alt="Open mHealth">
</a>


<a href="http://hl7.org/fhir">
<img style="float: right" width="25%" height="25%" src="http://build.fhir.org/assets/images/fhir-logo-www.png" alt="HL7 FHIR">
</a>

<br />

<h3 class="logoHeader" style="text-align: center">OMH to FHIR QuickStart Guide</h3>
</header>


<!-- wide style: to accomodate tables -->



# OMH to FHIR Mapper

This is an example Jupyter notebook file that maps OMH Schema instances to R4 FHIR Observation instances using:

1. A FHIR Observation profile instantiated as a Python FHIR r4 model library.
1. A mapping table between OMH datapoint Schema and FHIR Observation data elements.
1. A Concept Mapping table between OMH to FHIR concepts.

{%gist /Healthedata1/cd8686850ffedf0757bd030cea8f34e6 %}


Jupyter Notebook running in Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Healthedata1/mFHIR/master?filepath=mapping%2Fpython-mapping-example%2F)

Click on: "OMH to FHIR Mapping.ipynb“
Click the run button 2x
Scroll up to the copy paste box and follow the instructions.



[<<back](../README.md)