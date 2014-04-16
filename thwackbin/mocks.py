"""
    thwackbin.mocks
    ~~~~~~~~~~~~~~~

    Module contains static mock data returned by the service.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

from thwackbin import data


def project():
    return [{"id": 1, "name": "My Project", "url": "my-project"},
            {"id": 2, "name": "Another Project", "url": "another-project"},
            {"id": 64, "name": "Thanks for all the fish", "url": "thanks-for-all-the-fish"},
            {"id": 1023, "name": "Angry Birds", "url": "angry-birds"}]


def new_project():
    return dict(url="http://mock-url.com/not/real", id=1234)


def devices():
    return [
        {
            "os_name": "android",
            "large_image": "https://appthwack.com/appthwack/static/images/devices/large/acer-iconia-tab-a200.png",
            "multiplier": 1,
            "cpu_info": "1.0 GHz",
            "added": "2012-09-30 00:00:00",
            "heap_size": "256",
            "id": 135,
            "cpu_architecture_version": "ARMv7",
            "name": "Acer Iconia A200",
            "small_image": "https://appthwack.com/appthwack/static/images/devices/small/acer-iconia-tab-a200.png",
            "os_version": "4.0.3",
            "os_id": 1,
            "cpu_architecture_description": "ARMv7",
            "resolution": "1280 x 800"
        },
        {
            "os_name": "android",
            "large_image": "https://appthwack.com/appthwack/static/images/devices/large/acer-iconia-tab-a500.png",
            "multiplier": 1,
            "cpu_info": "1.0 GHz",
            "added": "2012-09-30 00:00:00",
            "heap_size": "256",
            "id": 27,
            "cpu_architecture_version": "ARMv7",
            "name": "Acer Iconia A500",
            "small_image": "https://appthwack.com/appthwack/static/images/devices/small/acer-iconia-tab-a500.png",
            "os_version": "4.0.3",
            "os_id": 1,
            "cpu_architecture_description": "ARMv7",
            "resolution": "800 x 1280"
        }]


def devicepool():
    return [{"id": 1, "name": "Only the Best"},
            {"id": 2, "name": "The Worst"},
            {"id": 15, "name": "The Usual Suspects"},
            {"id": 49, "name": "Tablets"}]


def file_id():
    return dict(file_id=64)


def run_id():
    return dict(run_id=128)


def runs():
    return [
        {
            "count": 40,
            "status": "completed",
            "initiator": "Thwack",
            "name": "HelloTrellis.apk (Jenkins)",
            "result": "fail",
            "failure_count": 15,
            "start_time": "05:09 PM",
            "public_url": None,
            "completed": 40,
            "warning_count": 0,
            "start_date": "April 15, 2014",
            "error_count": 0,
            "performance": None,
            "pass_count": 25,
            "status_text": "Completed",
            "id": 52366,
            "minutes_used": 24
        },
        {
            "count": 40,
            "status": "completed",
            "initiator": "Thwack",
            "name": "HelloTrellis.apk (Jenkins)",
            "result": "fail",
            "failure_count": 12,
            "start_time": "07:49 PM",
            "public_url": None,
            "completed": 40,
            "warning_count": 0,
            "start_date": "April 14, 2014",
            "error_count": 0,
            "performance": None,
            "pass_count": 28,
            "status_text": "Completed",
            "id": 52182,
            "minutes_used": 27
        }]


def results():
    return data.RESULTS


def cancellation():
    return dict(message='For great justice!')


def publish():
    return None


def compatibility():
    return {"compatible": [
        {
            "os_version": "4.3",
            "name": "Samsung Galaxy S III",
            "id": 60
        },
        {
            "os_version": "2.3.4",
            "name": "Samsung Galaxy S II",
            "id": 243
        }],
            "incompatible": [
                {
                    "os_version": "2.1-update1",
                    "reason": "Minimum SDK level not met",
                    "name": "Samsung Galaxy S",
                    "id": 73
                },
                {
                    "os_version": "2.1-update1",
                    "reason": "Minimum SDK level not met",
                    "name": "HTC Desire",
                    "id": 78
                }],
            "incompatible_count": 2,
            "total_device_count": 4,
            "compatible_count": 2}


if __name__ == '__main__':
    print results()
