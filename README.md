```bash
lar -c dump.fcl
```

https://internal.dunescience.org/doxygen/classgeo_1_1Geometry.html

Full HD
```bash
path-prepend /exp/dune/app/users/yuhw/dunecore/dunecore/Geometry FHICL_FILE_PATH
path-prepend /exp/dune/app/users/yuhw/dunecore/dunecore/Geometry/gdml FW_SEARCH_PATH
```


## 2025-03-03
https://github.com/LArSoft/larwirecell/blob/develop/larwirecell/Modules/Geometry/CTreeGeometry_module.cc

geo::WireReadoutGeom

**remember to replace all gdmls in the dumped tmp.fcl!**

Acutal information comes from `AuxDetGeometry`
but the name comes from `Geometry`
dunevd10kt_3view_30deg_v7_refactored_1x8x14.gdml
dunevd10kt_3view_30deg_v7_refactored_2x8x40.gdml

## Some convertion note from kratos:
```bash
wirecell-util convert-dunevd-wires dunevd10kt_3view_30deg_v1_1x6x6.txt dunevd10kt_3view_30deg_v1_1x6x6.json.bz2
wirecell-util plot-wires dunevd10kt_3view_30deg_v1_1x6x6.json.bz2 dunevd10kt_3view_30deg_v1_1x6x6.pdf

wirecell-util convert-dunevd-wires -t 3view dunevd10kt_3view_v1_1x6x6.txt dunevd10kt_3view_v1_1x6x6.json.bz2

wirecell-util convert-dunevd-wires -t 3view dunevd10kt_3view_v2_refactored_1x8x6ref.txt dunevd10kt_3view_v2_refactored_1x8x6ref.json.bz2
wirecell-util plot-wires dunevd10kt_3view_v2_refactored_1x8x6ref.json.bz2 dunevd10kt_3view_v2_refactored_1x8x6ref.pdf

wirecell-util convert-dunevd-wires -t 3view_30deg dunevd10kt_3view_30deg_v2_refactored_1x8x6ref.txt dunevd10kt_3view_30deg_v2_refactored_1x8x6ref.json.bz2
wirecell-util plot-wires dunevd10kt_3view_30deg_v2_refactored_1x8x6ref.json.bz2 dunevd10kt_3view_30deg_v2_refactored_1x8x6ref.pdf

wirecell-util convert-dunevd-wires -t 2view dunevd10kt_2view_v2_refactored_1x8x6ref.txt dunevd10kt_2view_v2_refactored_1x8x6ref.json.bz2
wirecell-util plot-wires dunevd10kt_2view_v2_refactored_1x8x6ref.json.bz2 dunevd10kt_2view_v2_refactored_1x8x6ref.pdf
```

## 2026-03-11
```bash
source /exp/dune/app/users/yuhw/setup.sh
path-prepend /exp/dune/app/users/yuhw/dunecore/dunecore/Geometry FHICL_FILE_PATH
path-prepend /exp/dune/app/users/yuhw/dunecore/dunecore/Geometry/gdml FW_SEARCH_PATH
# copy dunevd10kt_3view_30deg_v6_refactored.fcl to iceberg_v3_refactored.fcl
# replace dunevd10kt_3view_30deg_v6_refactored.gdml to iceberg_v3_refactored.gdml
lar -c iceberg_v3_refactored.fcl >& iceberg_v3_refactored.log

cp /exp/dune/app/users/mwang/iceberg/newgeom/icegeomv3-detsim.fcl ./iceberg_v3_refactored.fcl
# replace physics without input/outpu
lar -c iceberg_v3_refactored.fcl >& iceberg_v3_refactored.log
wirecell-util convert-multitpc-wires iceberg_v3_refactored.txt iceberg_v3_refactored.json.bz2
wirecell-util plot-wires iceberg_v3_refactored.json.bz2 iceberg_v3_refactored.pdf
wirecell-util plot-wires iceberg-wires-larsoft-v2.json.bz2 iceberg-wires-larsoft-v2.pdf
```