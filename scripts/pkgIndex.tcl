# Tcl package index file, version 1.1
# Do NOT edit by hand.  Let tcllib install generate this file.
# Generated by tcllib installer for version 1.6.1

# All tcllib packages need Tcl 8 (use [namespace])
if {![package vsatisfies [package provide Tcl] 8]} {return}

# Extend the auto_path to make tcllib packages available
if {[lsearch -exact $::auto_path $dir] == -1} {
    lappend ::auto_path $dir
}

# For Tcl 8.3.1 and later, that's all we need
if {[package vsatisfies [package provide Tcl] 8.4]} {return}
if {(0 == [catch {
    package vcompare [info patchlevel] [info patchlevel]
}]) && (
    [package vcompare [info patchlevel] 8.3.1] >= 0
)} {return}

# For older Tcl releases, here are equivalent contents
# of the pkgIndex.tcl files of all the modules

if {![package vsatisfies [package provide Tcl] 8.0]} {return}


set maindir $dir
set dir [file join $maindir beepcore] ;	 source [file join $dir pkgIndex.tcl]
set dir [file join $maindir FTP-1.2] ;	 source [file join $dir pkgIndex.tcl]
set dir [file join $maindir TclExpat-1.1] ;	 source [file join $dir pkgIndex.tcl]
set dir [file join $maindir TclXML-1.1.1] ;	 source [file join $dir pkgIndex.tcl]
unset maindir
