#!/usr/bin/env python
# encoding: utf-8

name = "C6H7_PES"
shortDesc = ""
longDesc = """

"""
autoGenerated=False
entry(
    index = 0,
    label = "n-C4H5 + C2H2 <=> benzene + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.373e+16,'cm^3/(mol*s)'), n=-1, Ea=(8.897,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(2.939e+16,'cm^3/(mol*s)'), n=-1.09, Ea=(9.26,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.373e+16,'cm^3/(mol*s)'), n=-1, Ea=(8.899,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.385e+16,'cm^3/(mol*s)'), n=-1, Ea=(8.901,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.692e+16,'cm^3/(mol*s)'), n=-1.03, Ea=(8.968,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.65e+16,'cm^3/(mol*s)'), n=-1.01, Ea=(9.481,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "n-C4H5 + C2H2 <=> fulvene + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.518e+15,'cm^3/(mol*s)'), n=-0.76, Ea=(8.768,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.518e+15,'cm^3/(mol*s)'), n=-0.76, Ea=(8.768,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.524e+15,'cm^3/(mol*s)'), n=-0.76, Ea=(8.77,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(4.625e+15,'cm^3/(mol*s)'), n=-0.89, Ea=(9.143,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.74e+19,'cm^3/(mol*s)'), n=-1.86, Ea=(12.384,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.235e+20,'cm^3/(mol*s)'), n=-2, Ea=(16.154,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "n-C4H5 + C2H2 <=> C6H6-3 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.12e+09,'cm^3/(mol*s)'), n=1.39, Ea=(17.334,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.144e+09,'cm^3/(mol*s)'), n=1.39, Ea=(17.342,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.457e+09,'cm^3/(mol*s)'), n=1.36, Ea=(17.442,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.126e+09,'cm^3/(mol*s)'), n=1.39, Ea=(17.334,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.101e+09,'cm^3/(mol*s)'), n=1.21, Ea=(18.014,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(2.975e+10,'cm^3/(mol*s)'), n=1.03, Ea=(19.443,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "n-C4H5 + C2H2 <=> C6H7-3",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,10,100],'atm'), arrhenius=[MultiArrhenius(arrhenius=[Arrhenius(A=(2.854e+48,'cm^3/(mol*s)'), n=-12.29, Ea=(15.703,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(3.493e-06,'cm^3/(mol*s)'), n=4.01, Ea=(-5.115,'kcal/mol'), T0=(1,'K'))]), MultiArrhenius(arrhenius=[Arrhenius(A=(1.439e+44,'cm^3/(mol*s)'), n=-10.08, Ea=(17.696,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.59e+44,'cm^3/(mol*s)'), n=-33.59, Ea=(-126.07,'kcal/mol'), T0=(1,'K'))]), MultiArrhenius(arrhenius=[Arrhenius(A=(4.631e+34,'cm^3/(mol*s)'), n=-6.68, Ea=(16.889,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(2.403e+27,'cm^3/(mol*s)'), n=-25.14, Ea=(-113.77,'kcal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "i-C4H5 + C2H2 <=> benzene + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(1.469e+23,'cm^3/(mol*s)'), n=-3.28, Ea=(24.909,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.469e+23,'cm^3/(mol*s)'), n=-3.28, Ea=(24.909,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.469e+23,'cm^3/(mol*s)'), n=-3.28, Ea=(24.909,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.668e+23,'cm^3/(mol*s)'), n=-3.3, Ea=(24.961,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(8.25e+24,'cm^3/(mol*s)'), n=-3.76, Ea=(26.565,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.372e+32,'cm^3/(mol*s)'), n=-5.84, Ea=(35.026,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "i-C4H5 + C2H2 <=> fulvene + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(6.504e+24,'cm^3/(mol*s)'), n=-3.44, Ea=(20.321,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(1.006e+34,'cm^3/(mol*s)'), n=-5.94, Ea=(28.788,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(6.504e+24,'cm^3/(mol*s)'), n=-3.44, Ea=(20.321,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(6.805e+24,'cm^3/(mol*s)'), n=-3.45, Ea=(20.339,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(9.696e+25,'cm^3/(mol*s)'), n=-3.76, Ea=(21.329,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.221e+41,'cm^3/(mol*s)'), n=-7.94, Ea=(39.601,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "i-C4H5 + C2H2 <=> C6H6-4 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(5.589e+18,'cm^3/(mol*s)'), n=-1.43, Ea=(30.344,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.679e+18,'cm^3/(mol*s)'), n=-1.43, Ea=(30.354,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(7.287e+18,'cm^3/(mol*s)'), n=-1.46, Ea=(30.468,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.589e+18,'cm^3/(mol*s)'), n=-1.43, Ea=(30.344,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.619e+19,'cm^3/(mol*s)'), n=-1.69, Ea=(31.437,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(4.703e+23,'cm^3/(mol*s)'), n=-2.73, Ea=(36.145,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "i-C4H5 + C2H2 <=> C6H6-5 + H",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([0.01,0.025,0.1,1,10,100],'atm'), arrhenius=[Arrhenius(A=(6.444e+15,'cm^3/(mol*s)'), n=-0.52, Ea=(38.442,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(6.444e+15,'cm^3/(mol*s)'), n=-0.52, Ea=(38.442,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(6.444e+15,'cm^3/(mol*s)'), n=-0.52, Ea=(38.442,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(6.624e+15,'cm^3/(mol*s)'), n=-0.53, Ea=(38.456,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(9.937e+15,'cm^3/(mol*s)'), n=-0.57, Ea=(38.651,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(5.673e+17,'cm^3/(mol*s)'), n=-1.04, Ea=(40.586,'kcal/mol'), T0=(1,'K'))]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "i-C4H5 + C2H2 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = PDepArrhenius(pressures=([1,10,100],'atm'), arrhenius=[MultiArrhenius(arrhenius=[Arrhenius(A=(1.144e+31,'cm^3/(mol*s)'), n=-9.21, Ea=(19.405,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(4.342e+39,'cm^3/(mol*s)'), n=-9.21, Ea=(19.212,'kcal/mol'), T0=(1,'K'))]), MultiArrhenius(arrhenius=[Arrhenius(A=(6.685e+51,'cm^3/(mol*s)'), n=-11.97, Ea=(29.669,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(3.601e+51,'cm^3/(mol*s)'), n=-28.03, Ea=(-70.559,'kcal/mol'), T0=(1,'K'))]), MultiArrhenius(arrhenius=[Arrhenius(A=(4.035e+42,'cm^3/(mol*s)'), n=-8.76, Ea=(28.822,'kcal/mol'), T0=(1,'K')), Arrhenius(A=(3.415e+41,'cm^3/(mol*s)'), n=-25.42, Ea=(-77.683,'kcal/mol'), T0=(1,'K'))])]),
    longDesc = 
"""
Originally from reaction library: Unclassified
""",
)

