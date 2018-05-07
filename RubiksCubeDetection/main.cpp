#include <stdio.h>
#include <string>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;

Mat src, srcGray;
Mat dst, detectedEdges;
Mat kernel;
std::vector<KeyPoint> keypoints;
std::vector<Vec3b> colorBins;
int pointColors[9];
int cube[6][9];
std::string faceNames[6] = {"Top", "Bottom", "Right", "Left", "Front", "Back"};

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
    // imshow("No longer Un-Canny", dst);
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

    detector->detect(dst, keypoints);

    // Mat im_with_keypoints;
    // drawKeypoints(dst, keypoints, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

    // // Show blobs
    // imshow("keypoints", im_with_keypoints);
}

bool sortPointsYX(KeyPoint a, KeyPoint b)
{
    if ((int)a.pt.y == (int)b.pt.y)
    {
        return (int)a.pt.x < (int)b.pt.x;
    }
    return (int)a.pt.y < (int)b.pt.y;
}

double colorComparison(Vec3b a, Vec3b b)
{
    int rDif = std::abs(a[0] - b[0]);
    int gDif = std::abs(a[1] - b[1]);
    int bDif = std::abs(a[2] - b[2]);
    return (rDif + gDif + bDif) / 3.0;
}

void detectColors()
{
    std::sort(keypoints.begin(), keypoints.end(), sortPointsYX);
    double colorThreshold = 5.0;
    for (int i = 0; i < 9; ++i)
    {
        Vec3b color = src.at<Vec3b>(keypoints[i].pt);
        if (colorBins.size() == 0)
        {
            colorBins.push_back(color);
            pointColors[i] = colorBins.size();
        }
        bool matchedBin = false;
        for (int j = 0; j < colorBins.size(); ++j)
        {
            Vec3b checkColor = colorBins[j];
            if (colorComparison(color, checkColor) < colorThreshold)
            {
                matchedBin = true;
                pointColors[i] = j;
            }
        }
        if (!matchedBin)
        {
            pointColors[i] = colorBins.size();
            colorBins.push_back(color);
        }
    }
}

void assignColors(int i)
{
    for (int j = 0; j < 9; ++j)
    {
        cube[i][j] = pointColors[j];
    }
}

void detectFace(int face)
{
    cvtColor(src, srcGray, CV_BGR2GRAY);

    CannyThreshold();
    while (keypoints.size() != 9)
    {
        blobDetector();
    }
    detectColors();
    assignColors(face);
}

void printColors()
{
    for (int i = 0; i < colorBins.size(); ++i)
    {
        Vec3b color = colorBins[i];
        std::cout << colorBins[i] << std::endl;
    }
}

void printCube()
{
    for (int i = 0; i < 6; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            std::cout << cube[i][j] << ' ';
        }
        std::cout << std::endl;
    }
}

int main()
{
    for (int i = 0; i < 6; ++i)
    {
        std::string filepath;
        std::cout << faceNames[i] << std::endl;
        std::cin >> filepath;
        src = imread(filepath);
        if (!src.data)
        {
            std::cout << "No image data" << std::endl;
            return -1;
        }
        detectFace(i);
    }
    printColors();
    printCube();
    // waitKey(0);
    return 0;
}