//
//  china_shift.h
//
//  Most code created by someone anonymous. Thank you, someone.
//  transformFromGCJToWGS() added by Fengzee (fengzee@fengzee.me).
//

#ifndef ChinaMapShift_ChinaMapShift_h
#define ChinaMapShift_ChinaMapShift_h

typedef struct {
    double lng;
    double lat;
} Location;

Location transformFromWGSToGCJ(Location wgLoc);
Location transformFromGCJToWGS(Location gcLoc);
Location bd_encrypt(Location gcLoc);
Location bd_decrypt(Location bdLoc);

#endif
