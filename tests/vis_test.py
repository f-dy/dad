import dad
from dad.utils import visualize_keypoints


def test_vis():
    detector = dad.load_DaD()
    img_path = "assets/0015_A.jpg"
    vis_path = "vis/0015_A_dad.jpg"
    visualize_keypoints(img_path, vis_path, detector, num_keypoints = 512)
