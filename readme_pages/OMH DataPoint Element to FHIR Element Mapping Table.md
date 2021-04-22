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

<style>.markdown-body { max-width: 1500px; }</style>


# OMH DataPoint Element to FHIR Element Mapping Table

The following table is used to map the OMH  header schema_id.name parameter  to the appropriate FHIR Observation `code` and `category`elements. See the [OMH Header Detailed Mapping](/KNSo9U0eTWaqLJRDqbKbWg) for an example.

{%gist Healthedata1/b58350049f4ff0575935f4f7a2d8e9e4 %}