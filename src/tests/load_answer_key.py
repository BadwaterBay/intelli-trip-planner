#!/usr/bin/env python

"""
# Load answer keys for testing
"""

from typing import List

# pylint: disable=line-too-long


def load_distance_matrix_origins_list() -> List[str]:
    """
    # Load origins of distance matrix
    """
    return [
        "Las Vegas McCarran International Airport, NV",
        "Los Angeles International Airport, CA",
        "Death Valley Furnace Creek Visitor Center, Furnace Creek, CA",
        "Mojave Kelso Depot Visitor Center, CA",
        "Joshua Tree National Park Visitor Center, Park Boulevard, Joshua Tree, CA",
        "Sequoia National Park - Visitor Center, Generals Highway, Three Rivers, CA",
        "Zion National Park Visitor Center, Zion – Mount Carmel Highway, Hurricane, UT",
        "Bryce Canyon National Park Visitor Center, Utah 63, Bryce Canyon City, UT",
        "Grand Canyon North Rim Visitor Center, AZ-67, North Rim, AZ",
        "Grand Canyon Visitor Center, South Entrance Road, Grand Canyon Village, AZ",
    ]


def load_distance_matrix_response():
    """
    # Load raw distance matrix response from Google Maps API
    """
    return {
        "destination_addresses": [
            "McCarran International Airport (LAS), 5757 Wayne Newton Blvd, Las Vegas, NV 89119, USA",
            "Los Angeles International Airport (LAX), 1 World Way, Los Angeles, CA 90045, USA",
            "Furnace Creek, CA 92328, USA",
            "90942 Kelso Cima Rd, Kelso, CA 92309, USA",
            "6554 Park Blvd, Joshua Tree, CA 92252, USA",
            "47050 Generals Hwy, Three Rivers, CA 93271, USA",
            "Zion national park, 1101 Zion \u2013 Mount Carmel Hwy, Hurricane, UT 84737, USA",
            "UT-63, Bryce Canyon City, UT 84764, USA",
            "129, AZ-67, North Rim, AZ 86023, USA",
            "S Entrance Rd, Grand Canyon Village, AZ 86023, USA",
        ],
        "origin_addresses": [
            "McCarran International Airport (LAS), 5757 Wayne Newton Blvd, Las Vegas, NV 89119, USA",
            "Los Angeles International Airport (LAX), 1 World Way, Los Angeles, CA 90045, USA",
            "Furnace Creek, CA 92328, USA",
            "90942 Kelso Cima Rd, Kelso, CA 92309, USA",
            "6554 Park Blvd, Joshua Tree, CA 92252, USA",
            "47050 Generals Hwy, Three Rivers, CA 93271, USA",
            "Zion national park, 1101 Zion \u2013 Mount Carmel Hwy, Hurricane, UT 84737, USA",
            "UT-63, Bryce Canyon City, UT 84764, USA",
            "129, AZ-67, North Rim, AZ 86023, USA",
            "S Entrance Rd, Grand Canyon Village, AZ 86023, USA",
        ],
        "rows": [
            {
                "elements": [
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "453 km", "value": 452812},
                        "duration": {"text": "4 hours 14 mins", "value": 15264},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "193 km", "value": 192690},
                        "duration": {"text": "2 hours 9 mins", "value": 7728},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "144 km", "value": 144369},
                        "duration": {"text": "1 hour 26 mins", "value": 5159},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "312 km", "value": 311544},
                        "duration": {"text": "3 hours 13 mins", "value": 11562},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "605 km", "value": 604974},
                        "duration": {"text": "6 hours 7 mins", "value": 22011},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "269 km", "value": 269142},
                        "duration": {"text": "2 hours 47 mins", "value": 10044},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "431 km", "value": 431026},
                        "duration": {"text": "4 hours 11 mins", "value": 15067},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "438 km", "value": 438044},
                        "duration": {"text": "4 hours 43 mins", "value": 16954},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "447 km", "value": 447211},
                        "duration": {"text": "4 hours 20 mins", "value": 15614},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "451 km", "value": 451120},
                        "duration": {"text": "4 hours 11 mins", "value": 15059},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "438 km", "value": 437724},
                        "duration": {"text": "4 hours 33 mins", "value": 16392},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "366 km", "value": 366440},
                        "duration": {"text": "3 hours 30 mins", "value": 12581},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "230 km", "value": 229653},
                        "duration": {"text": "2 hours 20 mins", "value": 8425},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "338 km", "value": 338302},
                        "duration": {"text": "3 hours 41 mins", "value": 13233},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "715 km", "value": 715338},
                        "duration": {"text": "6 hours 50 mins", "value": 24597},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "877 km", "value": 877222},
                        "duration": {"text": "8 hours 14 mins", "value": 29619},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "884 km", "value": 884240},
                        "duration": {"text": "8 hours 45 mins", "value": 31506},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "817 km", "value": 816997},
                        "duration": {"text": "7 hours 49 mins", "value": 28133},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "191 km", "value": 191247},
                        "duration": {"text": "2 hours 7 mins", "value": 7639},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "436 km", "value": 435684},
                        "duration": {"text": "4 hours 38 mins", "value": 16665},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "239 km", "value": 238990},
                        "duration": {"text": "2 hours 30 mins", "value": 8987},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "406 km", "value": 405970},
                        "duration": {"text": "4 hours 16 mins", "value": 15333},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "516 km", "value": 515548},
                        "duration": {"text": "5 hours 45 mins", "value": 20726},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "469 km", "value": 469067},
                        "duration": {"text": "4 hours 41 mins", "value": 16839},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "631 km", "value": 630950},
                        "duration": {"text": "6 hours 4 mins", "value": 21862},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "638 km", "value": 637969},
                        "duration": {"text": "6 hours 36 mins", "value": 23748},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "633 km", "value": 632563},
                        "duration": {"text": "6 hours 23 mins", "value": 22951},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "142 km", "value": 141782},
                        "duration": {"text": "1 hour 21 mins", "value": 4887},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "366 km", "value": 365989},
                        "duration": {"text": "3 hours 30 mins", "value": 12596},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "239 km", "value": 238765},
                        "duration": {"text": "2 hours 27 mins", "value": 8805},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "167 km", "value": 167175},
                        "duration": {"text": "1 hour 47 mins", "value": 6403},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "518 km", "value": 518151},
                        "duration": {"text": "5 hours 22 mins", "value": 19342},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "406 km", "value": 406001},
                        "duration": {"text": "4 hours 0 mins", "value": 14424},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "568 km", "value": 567884},
                        "duration": {"text": "5 hours 24 mins", "value": 19447},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "575 km", "value": 574902},
                        "duration": {"text": "5 hours 56 mins", "value": 21334},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "497 km", "value": 496696},
                        "duration": {"text": "4 hours 58 mins", "value": 17878},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "310 km", "value": 309863},
                        "duration": {"text": "3 hours 7 mins", "value": 11235},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "228 km", "value": 227823},
                        "duration": {"text": "2 hours 19 mins", "value": 8357},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "407 km", "value": 406651},
                        "duration": {"text": "4 hours 12 mins", "value": 15117},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "168 km", "value": 168080},
                        "duration": {"text": "1 hour 46 mins", "value": 6349},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "494 km", "value": 494206},
                        "duration": {"text": "5 hours 17 mins", "value": 18996},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "574 km", "value": 574081},
                        "duration": {"text": "5 hours 46 mins", "value": 20773},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "736 km", "value": 735965},
                        "duration": {"text": "7 hours 10 mins", "value": 25796},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "743 km", "value": 742983},
                        "duration": {"text": "7 hours 41 mins", "value": 27682},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "613 km", "value": 613004},
                        "duration": {"text": "5 hours 59 mins", "value": 21531},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "603 km", "value": 603285},
                        "duration": {"text": "6 hours 3 mins", "value": 21761},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "336 km", "value": 336174},
                        "duration": {"text": "3 hours 38 mins", "value": 13096},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "517 km", "value": 517201},
                        "duration": {"text": "5 hours 43 mins", "value": 20604},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "519 km", "value": 518604},
                        "duration": {"text": "5 hours 21 mins", "value": 19283},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "495 km", "value": 494847},
                        "duration": {"text": "5 hours 17 mins", "value": 18997},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "868 km", "value": 867503},
                        "duration": {"text": "8 hours 42 mins", "value": 31299},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,029 km", "value": 1029387},
                        "duration": {"text": "10 hours 5 mins", "value": 36321},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,036 km", "value": 1036405},
                        "duration": {"text": "10 hours 37 mins", "value": 38208},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "969 km", "value": 969162},
                        "duration": {"text": "9 hours 41 mins", "value": 34834},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "268 km", "value": 268459},
                        "duration": {"text": "2 hours 47 mins", "value": 9990},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "715 km", "value": 714826},
                        "duration": {"text": "6 hours 52 mins", "value": 24740},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "468 km", "value": 468458},
                        "duration": {"text": "4 hours 39 mins", "value": 16714},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "406 km", "value": 406383},
                        "duration": {"text": "4 hours 4 mins", "value": 14634},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "574 km", "value": 573558},
                        "duration": {"text": "5 hours 51 mins", "value": 21037},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "867 km", "value": 866987},
                        "duration": {"text": "8 hours 45 mins", "value": 31486},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "137 km", "value": 136765},
                        "duration": {"text": "1 hour 50 mins", "value": 6617},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "197 km", "value": 196587},
                        "duration": {"text": "2 hours 44 mins", "value": 9845},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "541 km", "value": 541398},
                        "duration": {"text": "5 hours 49 mins", "value": 20924},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "430 km", "value": 430493},
                        "duration": {"text": "4 hours 8 mins", "value": 14867},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "877 km", "value": 876860},
                        "duration": {"text": "8 hours 14 mins", "value": 29617},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "630 km", "value": 630491},
                        "duration": {"text": "6 hours 0 mins", "value": 21591},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "568 km", "value": 568416},
                        "duration": {"text": "5 hours 25 mins", "value": 19512},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "736 km", "value": 735592},
                        "duration": {"text": "7 hours 12 mins", "value": 25915},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,029 km", "value": 1029021},
                        "duration": {"text": "10 hours 6 mins", "value": 36364},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "137 km", "value": 137043},
                        "duration": {"text": "1 hour 51 mins", "value": 6643},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "255 km", "value": 254873},
                        "duration": {"text": "3 hours 9 mins", "value": 11351},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "600 km", "value": 599684},
                        "duration": {"text": "6 hours 14 mins", "value": 22429},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "437 km", "value": 437353},
                        "duration": {"text": "4 hours 40 mins", "value": 16806},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "884 km", "value": 883719},
                        "duration": {"text": "8 hours 46 mins", "value": 31556},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "637 km", "value": 637351},
                        "duration": {"text": "6 hours 32 mins", "value": 23530},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "575 km", "value": 575276},
                        "duration": {"text": "5 hours 58 mins", "value": 21451},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "742 km", "value": 742451},
                        "duration": {"text": "7 hours 44 mins", "value": 27854},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1,036 km", "value": 1035881},
                        "duration": {"text": "10 hours 38 mins", "value": 38303},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "197 km", "value": 196616},
                        "duration": {"text": "2 hours 44 mins", "value": 9818},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "255 km", "value": 254531},
                        "duration": {"text": "3 hours 8 mins", "value": 11284},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "477 km", "value": 477064},
                        "duration": {"text": "5 hours 10 mins", "value": 18581},
                        "status": "OK",
                    },
                ]
            },
            {
                "elements": [
                    {
                        "distance": {"text": "445 km", "value": 445127},
                        "duration": {"text": "4 hours 13 mins", "value": 15202},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "816 km", "value": 816114},
                        "duration": {"text": "7 hours 46 mins", "value": 27941},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "632 km", "value": 632335},
                        "duration": {"text": "6 hours 17 mins", "value": 22645},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "496 km", "value": 496453},
                        "duration": {"text": "4 hours 55 mins", "value": 17695},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "598 km", "value": 598105},
                        "duration": {"text": "5 hours 58 mins", "value": 21465},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "968 km", "value": 968276},
                        "duration": {"text": "9 hours 38 mins", "value": 34688},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "536 km", "value": 536307},
                        "duration": {"text": "5 hours 47 mins", "value": 20836},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "594 km", "value": 594223},
                        "duration": {"text": "6 hours 12 mins", "value": 22301},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "478 km", "value": 477601},
                        "duration": {"text": "5 hours 10 mins", "value": 18618},
                        "status": "OK",
                    },
                    {
                        "distance": {"text": "1 m", "value": 0},
                        "duration": {"text": "1 min", "value": 0},
                        "status": "OK",
                    },
                ]
            },
        ],
        "status": "OK",
    }


def load_parsed_distance_matrix_tuple() -> dict:
    """
    # Load parsed distance matrix as answer key
    """
    return {
        "distance": (
            (
                0,
                452812,
                192690,
                144369,
                311544,
                604974,
                269142,
                431026,
                438044,
                447211,
            ),
            (
                451120,
                0,
                437724,
                366440,
                229653,
                338302,
                715338,
                877222,
                884240,
                816997,
            ),
            (
                191247,
                435684,
                0,
                238990,
                405970,
                515548,
                469067,
                630950,
                637969,
                632563,
            ),
            (
                141782,
                365989,
                238765,
                0,
                167175,
                518151,
                406001,
                567884,
                574902,
                496696,
            ),
            (
                309863,
                227823,
                406651,
                168080,
                0,
                494206,
                574081,
                735965,
                742983,
                613004,
            ),
            (
                603285,
                336174,
                517201,
                518604,
                494847,
                0,
                867503,
                1029387,
                1036405,
                969162,
            ),
            (
                268459,
                714826,
                468458,
                406383,
                573558,
                866987,
                0,
                136765,
                196587,
                541398,
            ),
            (
                430493,
                876860,
                630491,
                568416,
                735592,
                1029021,
                137043,
                0,
                254873,
                599684,
            ),
            (
                437353,
                883719,
                637351,
                575276,
                742451,
                1035881,
                196616,
                254531,
                0,
                477064,
            ),
            (
                445127,
                816114,
                632335,
                496453,
                598105,
                968276,
                536307,
                594223,
                477601,
                0,
            ),
        ),
        "duration": (
            (0, 15264, 7728, 5159, 11562, 22011, 10044, 15067, 16954, 15614),
            (15059, 0, 16392, 12581, 8425, 13233, 24597, 29619, 31506, 28133),
            (7639, 16665, 0, 8987, 15333, 20726, 16839, 21862, 23748, 22951),
            (4887, 12596, 8805, 0, 6403, 19342, 14424, 19447, 21334, 17878),
            (11235, 8357, 15117, 6349, 0, 18996, 20773, 25796, 27682, 21531),
            (21761, 13096, 20604, 19283, 18997, 0, 31299, 36321, 38208, 34834),
            (9990, 24740, 16714, 14634, 21037, 31486, 0, 6617, 9845, 20924),
            (14867, 29617, 21591, 19512, 25915, 36364, 6643, 0, 11351, 22429),
            (16806, 31556, 23530, 21451, 27854, 38303, 9818, 11284, 0, 18581),
            (15202, 27941, 22645, 17695, 21465, 34688, 20836, 22301, 18618, 0),
        ),
    }


def load_parsed_distance_matrix_list() -> dict:
    """
    # Load parsed distance matrix (list) as answer key
    """
    distance_matrix: dict = load_parsed_distance_matrix_tuple()
    return {
        "distance": list(map(list, distance_matrix["distance"])),
        "duration": list(map(list, distance_matrix["duration"])),
    }
