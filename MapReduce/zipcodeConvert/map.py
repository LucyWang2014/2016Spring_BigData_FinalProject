#!/usr/bin/python

import sys
from datetime import datetime

import traceback

ids = [
[0.0,0.0],[-74.0059413,40.7127837],[-73.8713099,40.6056632],[-73.8624893,40.8637435],[-73.9785952,40.7260601],[-74.1739057,40.5567951],[-74.0704232,40.5967312],[-73.9234619,40.7643574],[-73.9215888,40.7796684],[-73.7860276,40.754115],[-73.7852922,40.6755827],[-74.0035709,40.602196],[-74.0170279,40.7032775],[-74.0160576,40.7122172],[-74.0329499,40.6261638],[-73.7801447,40.7828828],[-73.7654367,40.7585569],[-73.9561495,40.6536822],[-73.8856912,40.8700999],[-73.7154014,40.7243707],[-73.88601,40.8523198],[-73.9976946,40.6112691],[-73.9976946,40.6112691],[-74.1885825,40.6208143],[-73.9697795,40.7988958],[-73.9844722,40.6848689],[-73.9888797,40.6323009],[-73.9262483,40.5564945],[-73.8154394,40.7089491],[-73.9596565,40.5780706],[-73.8213213,40.6158335],[-73.8742531,40.8604899],[-73.8665241,40.8506558],[-73.9932872,40.6960105],[-73.9716271,40.7051744],[-73.9095279,40.66308],[-73.9212858,40.6944282],[-73.9212858,40.6944282],[-73.7330753,40.692158],[-73.9060579,40.6402325],[-73.9991637,40.6795331],[-73.9216971,40.7934744],[-73.9216971,40.7934744],[-73.9741874,40.7711329],[-74.2355404,40.5281967],[-73.9970307,40.7157509],[-73.7874983,40.8468202],[-73.9036487,40.840047],[-73.9918181,40.7637581],[-73.9639021,40.6893665],[-73.9918181,40.7637581],[-73.8281865,40.8749698],[-73.9962255,40.686536],[-73.8389657,40.786395],[-74.0060624,40.6781015],[-73.9859414,40.5749261],[-73.8642613,40.7449859],[-73.8642613,40.7449859],[-73.8213213,40.8430539],[-73.8925983,40.8391133],[-73.8921959,40.8366558],[-73.9447994,40.6681032],[-73.9447994,40.6681032],[-73.8801301,40.6836118],[-73.7470765,40.768713],[-73.984518,40.6960191],[-73.9881451,40.7033164],[-74.0153231,40.6187181],[-74.0013737,40.7465004],[-73.9227554,40.8316761],[-73.8713099,40.7737505],[-73.9301037,40.6437474],[-73.9301037,40.6437474],[-73.8095574,40.7525589],[-73.9389213,40.7957399],[-73.9389213,40.7957399],[-73.8830701,40.6568312],[-73.8830701,40.6568312],[-73.8909693,40.8453781],[-73.9815337,40.7264773],[-73.9330429,40.7158762],[-73.8272029,40.883324],[-73.8801301,40.737975],[-73.8801301,40.737975],[-74.156292,40.5394463],[-73.952894,40.6496327],[-73.7448437,40.5998931],[-74.0112764,40.7074909],[-74.0112764,40.7074909],[-73.9624327,40.6409217],[-73.9896986,40.7410605],[-73.9330429,40.6268432],[-73.833079,40.7674987],[-73.8448469,40.7428054],[-73.8905425,40.8614658],[-73.8448469,40.718106],[-73.8566087,40.7000227],[-73.9741874,40.6920638],[-73.7801447,40.7335179],[-74.186124,40.577455],[-73.9916342,40.7547072],[-73.7118223,40.7471504],[-73.8804427,40.698994],[-74.016792,40.6894501],[-74.0395587,40.6994748],[-74.0450675,40.6900495],[-73.9903489,40.6733364],[-73.9860914,40.7376121],[-73.977126,40.5910166],[-74.156292,40.5543273],[-74.1269322,40.5502073],[-73.995692,40.659017],[-73.9418603,40.7245448],[-74.0027418,40.7335719],[-74.0027418,40.7335719],[-74.0916944,40.6146432],[-73.9496079,40.8259597],[-73.8080869,40.5879465],[-74.1680347,40.5807663],[-73.9271644,40.8384699],[-73.9332427,40.8433959],[-73.7977928,40.7212372],[-73.762495,40.7112203],[-73.958372,40.5942226],[-73.8429989,40.6571222],[-74.0074731,40.7265834],[-73.8801301,40.8120246],[-73.9212019,40.8677145],[-73.9256948,40.8715417],[-73.8830701,40.7556818],[-73.7889689,40.702677],[-73.7742616,40.7178539],[-73.7781391,40.6413111],[-73.9741874,40.6376415],[-73.8272029,40.705695],[-73.8106854,40.7384986],[-73.9027286,40.8739998],[-73.9800645,40.7423292],[-73.8739659,40.7769271],[-73.7448437,40.6740861],[-73.967557,40.7675915],[-73.967557,40.7675915],[-73.9844722,40.773828],[-73.9844722,40.773828],[-73.9973273,40.7191413],[-73.9485424,40.744679],[-73.9485424,40.744679],[-73.8915875,40.8248438],[-73.9842724,40.715033],[-73.9492079,40.6056249],[-73.9389213,40.578158],[-73.9586849,40.802479],[-73.9558333,40.8169443],[-73.9102628,40.8761173],[-73.9330429,40.6119911],[-73.9330429,40.6119911],[-74.156292,40.6336287],[-73.9065883,40.7294018],[-74.0076108,40.7409865],[-73.9168766,40.8209719],[-73.87425,40.717372],[-73.9784137,40.7553676],[-73.9668408,40.7540369],[-73.9840195,40.7549309],[-73.9840195,40.7549309],[-73.9653715,40.6190629],[-73.9624327,40.8089564],[-73.9109977,40.8250663],[-73.9228881,40.8091068],[-73.9051185,40.8488863],[-73.9756567,40.7478792],[-73.8036752,40.7665245],[-74.115187,40.5733493],[-73.8624893,40.7502698],[-73.8786601,40.8771463],[-73.758241,40.7408584],[-74.115187,40.5584751],[-73.9686534,40.6130962],[-73.9736312,40.6424282],[-73.8927255,40.7331241],[-73.8507279,40.6794072],[-73.9805817,40.6681038],[-73.8566087,40.8382522],[-73.8330844,40.8496714],[-73.7972,40.8615],[-73.8639594,40.8553279],[-73.993519,40.750568],[-74.1254641,40.6354914],[-73.9506774,40.6590448],[-73.9668408,40.6774196],[-73.9689558,40.6602037],[-73.7419017,40.7156628],[-73.940358,40.7509287],[-73.9484021,40.7566953],[-73.9212858,40.7932271],[-74.0094471,40.6772802],[-73.8624893,40.7255722],[-73.8272029,40.6958108],[-73.9018292,40.7043986],[-73.88601,40.7931277],[-73.9109977,40.8940853],[-73.8372237,40.5797863],[-73.9509934,40.7605031],[-73.7389596,40.6584068],[-74.2032581,40.5509808],[-73.7654367,40.6894086],[-74.0799469,40.6427017],[-73.7948516,40.7282239],[-73.8330844,40.8348809],[-74.0025502,40.710322],[-73.9536163,40.5975847],[-74.0029883,40.723301],[-73.8683697,40.8251411],[-73.8683697,40.8251411],[-74.0738631,40.5829024],[-73.7919103,40.6808594],[-73.8124984,40.6764003],[-73.9701967,40.7085692],[-73.7683784,40.6626441],[-73.7683784,40.6626441],[-73.9154069,40.8811637],[-74.0784785,40.6288778],[-74.0065189,40.7516034],[-73.9037477,40.7745459],[-73.9778494,40.7316903],[-73.9330981,40.6882279],[-73.9196324,40.7432759],[-74.0123851,40.645532],[-74.0123851,40.645532],[-73.961698,40.7576281],[-73.9844722,40.759011],[-74.0086323,40.7162692],[-73.99696,40.7107469],[-73.9712488,40.7830603],[-73.990382,40.735654],[-73.9109977,40.8595861],[-73.9565551,40.7735649],[-73.9565551,40.7735649],[-73.9753676,40.7870106],[-73.9753676,40.7870106],[-73.8859514,40.8979346],[-73.8935548,40.884307],[-73.8668996,40.8458888],[-73.9393554,40.8417082],[-73.9393554,40.8417082],[-74.1093141,40.6270298],[-74.0013737,40.7465004],[-73.9227554,40.8316761],[-73.8816001,40.8430609],[-74.0035709,40.735781],[-73.8695474,40.8309653],[-74.1386767,40.616296],[-73.8095574,40.7920449],[-73.840436,40.7606911],[-73.8566087,40.8776859],[-73.964,40.7194016],[-73.9517335,40.7079936],[-73.9756567,40.6539346],[-73.8566087,40.6901366],[-73.862916,40.895361],[-73.9036487,40.7512123],[-74.0131196,40.7118011],[-73.9492079,40.7762231],[-73.9492079,40.7762231],[-74.2126853,40.5089712],[-74.2126853,40.5089712]]


def get_lat_long(ln):
    return (','.join(ln[:9]), (float(ln[9]), float(ln[10])), (float(ln[11]), float(ln[12])), ','.join(ln[13:]))


def convert_to_id(tup):
    diff = map(lambda x: (x[0]-tup[0])**2+(x[1]-tup[1])**2, ids)
    diff[0] = 10e5
    mindiff = reduce(lambda x,y: x if x[1]<y[1] else y, enumerate(diff))
    imin = mindiff[0]
    return str(imin)


def process(x):
    try:
        x = x.strip().split(',')
        lat_long = get_lat_long(x)
        new_str = ','.join([lat_long[0], convert_to_id(lat_long[1]), convert_to_id(lat_long[2]), lat_long[3]])
        return new_str
    except:
        traceback.print_exc()
        pass


for line in sys.stdin:
    _line = process(line)

        print(line)