from obs_vc_grabber import OBSGrabber

def main():
    try:
        grabber = OBSGrabber()
        grab_area = {"width": 1280, "height": 720}
        frame = grabber.get_frame(grab_area)
        
        import cv2
        cv2.imshow("OBS Frame", frame)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
    
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()