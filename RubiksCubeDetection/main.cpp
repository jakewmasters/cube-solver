#include <stdio.h>
#include <string>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

Mat src, srcGray;
Mat dst, detectedEdges;
Mat kernel;

void CannyThreshold()
{
    Mat blurredImage;
    blur(srcGray, blurredImage, Size(3, 3));
    int threshold = 20;
    Canny(blurredImage, detectedEdges, threshold, threshold * 3, 3);
    kernel = (Mat_<uchar>(3, 3) << 0, 1, 0, 1, 1, 1, 0, 1, 0);
    dilate(detectedEdges, detectedEdges, kernel);
    dst = Scalar::all(0);
    srcGray.copyTo(dst, detectedEdges);
    imshow("No longer Un-Canny", dst);
}

void blobDetector()
{
    SimpleBlobDetector::Params params;

    params.minThreshold = 10;
    params.maxThreshold = 1000;

    params.filterByArea = true;
    params.minArea = 50;

    // Filter by Circularity
    params.filterByCircularity = false;
    params.minCircularity = 0.05;

    // Filter by Convexity
    params.filterByConvexity = false;
    params.minConvexity = 0;

    // Filter by Inertia
    params.filterByInertia = false;
    params.minInertiaRatio = 0.1;

    Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);
    std::vector<KeyPoint> keypoints;

    detector->detect(dst, keypoints);

    cout << to_string(keypoints.length);

    // Mat im_with_keypoints;
    // drawKeypoints(dst, keypoints, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

    // // Show blobs
    // imshow("keypoints", im_with_keypoints);
}

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    src = imread(argv[1], 1);
    if (!src.data)
    {
        printf("No image data \n");
        return -1;
    }

    cvtColor(src, srcGray, CV_BGR2GRAY);

    CannyThreshold();
    blobDetector();
    waitKey(0);
    return 0;
}