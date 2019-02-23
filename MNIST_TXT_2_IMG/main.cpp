#include <iostream>
#include <string>
#include <bitset>
#include <list>
#include <fstream>
#include <iomanip>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


using namespace cv;
using namespace std;

int str2int (string str){
	stringstream geek(str); 
	int x = 0; 
	geek >> x; 
	return x;
}

void
dumpImage(Mat& img, char* fname)
{
	ofstream ofs;
	ofs.open(fname,std::ofstream::out);
	unsigned short pix = 0;
	for(int i = 0; i < img.rows; i++){
		for(int j = 0; j < img.cols; j++ ){
			pix = img.at<unsigned short>(i, j);
			//ofs << pix << " ";
			ofs << pix << std::endl;
		}
		//ofs << std::endl;
	}
	ofs.close();
}

int main(int argc, char* argv[]){

	ifstream fin;
	char cline[100];
	int magic = -1;
	int nitems = -1;
	int row = -1;
	int col = -1;
	bool done = false;
	fin.open(argv[1], std::ifstream::in);
	int nrow = 0;
	int ncol = 0;
	int ipix = 0;
	int imageC = 0;
	int count = atoi(argv[2]);
	Mat image(28, 28, CV_16UC1);
	if(fin.is_open()){
		while(!fin.eof()){
			fin.getline(cline, 100);
			string sline(cline);
			//std::cout << sline << std::endl;
			if(!done){
				std::size_t found = sline.find_last_of(":");
				string si = sline.substr(found+1);
				int i = str2int(si);
				std::cout << i << std::endl;
				if (magic < 0)
					magic = i;
				else if (nitems < 0)
					nitems = i;
				else if (row < 0)
					row = i;
				else if (col < 0){
					col = i;
					done = true;
					//ipix = row * col;
				}	
			}

			if(done){
				unsigned short pix = str2int(sline);
				ipix ++; 
				if(ncol == col-1)
					nrow ++;
				ncol ++;
				if(nrow >= row)
					nrow = 0;
				if(ncol >= col)
					ncol = 0;
				if(nrow == 0 && ncol == 0){
					char ofname[100];
					sprintf(ofname, "image_data/%d_img.bmp", imageC);
					std::cout << "Writing to:" << ofname << std::endl;
					imwrite(ofname, image);
					sprintf(ofname, "image_data/%d_img.txt", imageC);
					dumpImage(image, ofname);
					if(imageC == count)
						exit(1);
					imageC++;
					ipix = 0;
				}
				std::cout << pix << "(" << nrow << ", " << ncol << ")" << std::endl;
				image.at<unsigned short int>(nrow, ncol) = pix;

			}

		}
	}
	return 0;
}



