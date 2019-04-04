"""Structural Similarity (SSIM)
Computing the structural similarity of the images."""

from skimage.measure import compare_ssim
import imutils
import cv2
from sift.comparison.toolbox import cropping_images

def compare(original_fname, archived_fname):
    original = cv2.imread(original_fname)
    archived = cv2.imread(archived_fname)

    if original is not None and archived is not None:
        original_cropped, archived_cropped = cropping_images(original, archived)
        original_gray = cv2.cvtColor(original_cropped, cv2.COLOR_BGR2GRAY)
        archived_gray = cv2.cvtColor(archived_cropped, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(original_gray, archived_gray, full=True)
    return (score, None)
