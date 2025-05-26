import os
import glob
import numpy as np
import pandas as pd
import requests
from urllib import response
from datetime import *
from concurrent.futures import ThreadPoolExecutor
from PyPDF2 import *
from PyPDF2.errors import PdfReadError