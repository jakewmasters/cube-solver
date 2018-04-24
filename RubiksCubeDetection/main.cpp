#include <stdio.h>
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;

Mat src, srcGray;
Mat dst, detectedEdges;
Mat kernel;

void CannyThreshold()
{
    Mat blurredImage;
    blur(srcGray, blurredImage, Size(3, 3));
    int threshold = 20;
    Canny(blurredImage, detectedEdges, threshold, threshold*3, 3);
    kernel = (Mat_<uchar>(3,3) << 0,1,0,1,1,1,0,1,0);
    dilate(detectedEdges, detectedEdges, kernel);
    dst = Scalar::all(0);
    srcGray.copyTo(dst, detectedEdges);
    imshow("No longer Un-Canny", dst);
}

//void SudokuMethod()
//{
//    Mat outerBox = Mat(src.size(), CV_8UC1);
//    Mat blurredImage;
//    GaussianBlur(srcGray, blurredImage, Size(11,11), 0);
//    adaptiveThreshold(srcGray, outerBox, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 5, 5);
//    bitwise_not(outerBox, outerBox);
//    kernel = (Mat_<uchar>(3,3) << 0,1,0,1,1,1,0,1,0);
//    dilate(outerBox, outerBox, kernel);
//    imshow("Otter box", outerBox);
//}

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    src = imread( argv[1], 1 );
    if ( !src.data )
    {
        printf("No image data \n");
        return -1;
    }

    cvtColor(src, srcGray, CV_BGR2GRAY);

    CannyThreshold();
//    SudokuMethod();
    waitKey(0);
    return 0;
}