|Source = OMH Schema|Target = FHIR Element|FHIR Quantity Pattern or ValueSet(binding strength)|FHIR Example
|---|---|---|---|
|[activity-name]({{page.omlschema_url}}activity-name-1.0.json)|[string][string]|
|[date-time]({{page.omlschema_url}}date-time-1.0.json)|[dateTime][dateTime]|
|[full-date]({{page.omlschema_url}}full-date-1.0.json)|[dateTime][dateTime]|
|[local-time]({{page.omlschema_url}}local-time-1.0.json)|[string][string]|
|[body-location]({{page.omlschema_url}}body-location-1.0.json)|[code][code]|[body-location](valueset-body-location.html)||
|[body-posture]({{page.omlschema_url}}body-posture-1.0.json)|[code][code]|[body-posture](valueset-body-posture.html)||
|[day-of-week]({{page.omlschema_url}}day-of-week-1.0.json)|[code][code]|[day-of-week](valueset-day-of-week.html)||
|[descriptive-statistic]({{page.omlschema_url}}descriptive-statistic-1.0.json)|[code][code]|[descriptive-statistic]{{site.data.fhir.path}}/valueset-observation-statistics.html)||
|[descriptive-statistic-denominator]({{page.omlschema_url}}descriptive-statistic-denominator-1.0.json)|[code][code]|[descriptive-statistic-denominator](valueset-descriptive-statistic-denominator.html)||
|[intervention-administration-route]({{page.omlschema_url}}intervention-administration-route-1.0.json)|[code][code]|[intervention-administration-route](valueset-intervention-administration-route.html)||
|[medication-dose-unit]({{page.omlschema_url}}medication-dose-unit-1.0.json)|[code][code]|[medication-dose-unit](valueset-medication-dose-unit.html)||
|[part-of-day]({{page.omlschema_url}}part-of-day-1.0.json)|[code][code]|[part-of-day](valueset-part-of-day.html)||
|[position-during-measurement]({{page.omlschema_url}}position-during-measurement-1.0.json)|[code][code]|[position-during-measurement](valueset-position-during-measurement.html)||
|[specimen-source]({{page.omlschema_url}}specimen-source-1.0.json)|[code][code]|[specimen-source](valueset-specimen-source.html)||
|[temporal-relationship-to-meal]({{page.omlschema_url}}temporal-relationship-to-meal-1.0.json)|[code][code]|[temporal-relationship-to-meal](valueset-temporal-relationship-to-meal.html)||
|[temporal-relationship-to-physical-activity]({{page.omlschema_url}}temporal-relationship-to-physical-activity-1.0.json)|[code][code]|[temporal-relationship-to-physical-activity](valueset-temporal-relationship-to-physical-activity.html)||
|[temporal-relationship-to-sleep]({{page.omlschema_url}}temporal-relationship-to-sleep-1.0.json)|[code][code]|[temporal-relationship-to-sleep](valueset-temporal-relationship-to-sleep.html)||
|[acceleration-unit-value-1.0.json]({{page.omlschema_url}}acceleration-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"m/s^2","system":"http://unitsofmeasure.org","code":"m/s2"}|
|[angular-velocity-unit-value-1.0.json]({{page.omlschema_url}}angular-velocity-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"ad/s","system":"http://unitsofmeasure.org","code":"ad/s"}
|[area-unit-value-1.0.json]({{page.omlschema_url}}area-unit-value-1.0.json)|[Quantity][Quantity]|[area-unit-value](valueset-area-unit-value.html) ([required][required])||
|[duration-unit-value-1.0.json]({{page.omlschema_url}}duration-unit-value-1.0.json)|[Quantity][Quantity]|[duration-unit-value](valueset-duration-unit-value.html) ([required][required])||
|[duration-unit-value-range-1.0.json]({{page.omlschema_url}}duration-unit-value-range-1.0.json)|[Range][Range]|[duration-unit-value](valueset-duration-unit-value.html) ([required][required])||
|[frequency-unit-value-1.0.json]({{page.omlschema_url}}frequency-unit-value-1.0.json)|[Ratio][Ratio]|[duration-unit-value](valueset-duration-unit-value.html) ([required][required])||
|[kcal-unit-value-1.0.json]({{page.omlschema_url}}kcal-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"kcal","system":"http://unitsofmeasure.org","code":"kcal"}
|[length-unit-value-1.0.json]({{page.omlschema_url}}length-unit-value-1.0.json)|[Quantity][Quantity]|[length-unit-value](valueset-length-unit-value.html) ([required][required])||
|[magnetic-flux-density-unit-value-1.0.json]({{page.omlschema_url}}magnetic-flux-density-unit-value-1.0.json)|[Quantity][Quantity]|[magnetic-flux-density-unit-value](valueset-magnetic-flux-density-unit-value.html) ([required][required])||
|[mass-unit-value-1.0.json]({{page.omlschema_url}}mass-unit-value-1.0.json)|[Quantity][Quantity]|[mass-unit-value](valueset-mass-unit-value.html) ([required][required])||
|[medication-dose-unit-value-1.0.json]({{page.omlschema_url}}medication-dose-unit-value-1.0.json)|[Quantity][Quantity]|[medication-dose-unit](valueset-medication-dose-unit.html) ([extensible][extensible])||
|[medication-dose-unit-value-range-1.0.json]({{page.omlschema_url}}medication-dose-unit-value-range-1.0.json)|[Range][Range]|[medication-dose-unit-value](valueset-medication-dose-unit.html) ([extensible][extensible])||
|[pace-unit-value-1.0.json]({{page.omlschema_url}}pace-unit-value-1.0.json)|[Quantity][Quantity]|[pace-unit-value](valueset-pace-unit-value.html) ([required][required])||
|[plane-angle-unit-value-1.0.json]({{page.omlschema_url}}plane-angle-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"deg","system":"http://unitsofmeasure.org","code":"deg"}
|[speed-unit-value-1.0.json]({{page.omlschema_url}}speed-unit-value-1.0.json)|[Quantity][Quantity]|[speed-unit-value](valueset-speed-unit-value.html) ([required][required])||
|[temperature-unit-value-1.0.json]({{page.omlschema_url}}temperature-unit-value-1.0.json)|[Quantity][Quantity]|[temperature-unit-value](valueset-temperature-unit-value.html) ([required][required])||
|[unit-value-1.0.json]({{page.omlschema_url}}unit-value-1.0.json)|[Quantity][Quantity]|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html) ([required][required])||
|[unit-value-range-1.0.json]({{page.omlschema_url}}unit-value-range-1.0.json)|[Range][Range]|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html) ([required][required])||
|[volume-unit-value-1.0.json]({{page.omlschema_url}}volume-unit-value-1.0.json)|[Quantity][Quantity]|[volume-unit-value](valueset-volume-unit-value.html) ([required][required])||
|[time-frame-1.0.json]({{page.omlschema_url}}time-frame-1.0.json)|[dateTime][dateTime]\|[Period]({{site.data.fhir.path}}/datatypes.html#Period)||
|[time-interval-1.0.json]({{page.omlschema_url}}time-interval-1.0.json)|\|[Period]({{site.data.fhir.path}}/datatypes.html#Period)||
{:.grid}
